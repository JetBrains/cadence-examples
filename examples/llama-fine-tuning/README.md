# Llama Fine-Tuning Example

This example demonstrates how to fine-tune the Mistral-7B language model using LoRA (Low-Rank Adaptation) technique.

## Prerequisites

Before running this example, you need to:

1. Set the `HF_TOKEN` environment variable with your Hugging Face API token
   - You can get your token from: https://huggingface.co/settings/tokens
   - This token is required to download the model from Hugging Face

```bash
export HF_TOKEN=your_hugging_face_token
```

## How to run

Navigate to the `llama-fine-tuning` directory and run the following command:

```bash
cadence execution start --preset llama-fine-tuning.yaml
```

This will provision the required resources (H200 GPU), set up the environment, and execute the fine-tuning script.
