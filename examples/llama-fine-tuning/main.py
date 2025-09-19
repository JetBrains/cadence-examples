import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig
from peft import LoraConfig
from datasets import load_dataset
from trl import SFTTrainer, SFTConfig

# Load the Mistral-7B model
model_id = "mistralai/Mistral-7B-v0.1"

quantization_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_compute_dtype=torch.float16,
    bnb_4bit_quant_type="nf4"
)

# Load model with quantization
model = AutoModelForCausalLM.from_pretrained(model_id, quantization_config=quantization_config)

# Load tokenizer
tokenizer = AutoTokenizer.from_pretrained(model_id)
tokenizer.pad_token = tokenizer.eos_token

lora_config = LoraConfig(
    r=8,
    target_modules=["q_proj", "o_proj", "k_proj", "v_proj", "gate_proj", "up_proj", "down_proj"],
    bias="none",
    task_type="CAUSAL_LM",
)

# Apply LoRA adapter
model.add_adapter(lora_config)

# Load dataset
train_dataset = load_dataset("stingning/ultrachat", split="train[:1%]")

# Training configuration
training_arguments = SFTConfig(
    output_dir="./outputs",
    per_device_train_batch_size=4,
    gradient_accumulation_steps=4,
    optim="paged_adamw_32bit",
    save_steps=10,
    logging_steps=1,
    learning_rate=2e-4,
    max_grad_norm=0.3,
    max_steps=30,
    warmup_ratio=0.03,
    lr_scheduler_type="constant",
    gradient_checkpointing=True,
    max_length=512,
    packing=True,
    report_to="none",  # report_to="wandb"
)


def formatting_func(example):
    text = ""
    for idx, msg in enumerate(example["data"]):
        if idx % 2 == 0:
            text += f"<|user|>\n{msg}{tokenizer.eos_token}\n"
        else:
            text += f"<|assistant|>\n{msg}{tokenizer.eos_token}\n"
    return text


trainer = SFTTrainer(
    model=model,
    args=training_arguments,
    train_dataset=train_dataset,
    processing_class=tokenizer,
    formatting_func=formatting_func,
)
trainer.train()
