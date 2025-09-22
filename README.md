# Cadence CLI

## Install

```shell
pip install jetbrains-cadence
```

This will create a `cadence` script in your current environment.

## Getting Started

```shell
cadence login
```

If you want to use Cadence CLI in the non-interactive environment, you
can [create the token manually](https://api.cadence.jetbrains.com/app/jettrain/token.html) and pass it via
`CADENCE_TOKEN` environment variable

### Start the execution from YAML config
Start the execution with:
```shell
cadence execution start --preset path/to/config.yaml
```

This will print the ID of the started execution.\
Config file format is described [here](#config-file-format).\
Available cloud resources are described [here](#resources).

### Examples

- [Basic example](examples/basic) - Simple example that only uses default storage.
- [Llama fine-tuning example](examples/llama-fine-tuning) - Example demonstrating how to fine-tune the Mistral-7B
  language model using LoRA.
- [Complex example](examples/complex) - Advanced example with custom storage and more complex configuration.

## Available Commands

#### See the execution status

```shell
cadence execution status <YOUR-EXECUTION-ID>
```

#### Stop the execution

```shell
cadence execution stop <YOUR-EXECUTION-ID>
```

#### Get information about the execution as a JSON

```shell
cadence execution info <YOUR-EXECUTION-ID>
```

#### List executions

```shell
cadence execution list
```

Options:

```
  --offset INTEGER  [default: 0]
  --count INTEGER   [default: 50]
  --all             List all executions. Count and offset are ignored
  --json / --table  Output format  [default: table]
```

#### View execution logs

```shell
cadence execution logs <YOUR-EXECUTION-ID>
```

#### Open terminal

```shell
cadence execution terminal <YOUR-EXECUTION-ID>
```

#### Download data

```shell
cadence execution download <YOUR-EXECUTION-ID>
```

Options:

```
  --to DIRECTORY  [required]
  --inputs        Include inputs
  --no-outputs    Exclude outputs
```

### Workspace management

#### Display information about the current workspace:

```shell
cadence workspace
```

#### See available workspaces:

```shell
cadence workspace list
```

#### Set workspace:

```shell
cadence workspace set <YOUR-WORKSPACE-ID>
```

## Config file format:

```yaml
working_dir: string       # Required.
cmd: # Commands to run in sequence. Required.
  - string
description: string


# Provisioning configuration. Required.
# Must be one of the available resources.
provisioning:
  gpu_type: string | null # Required.
  gpu_count: int | null   # Required.
  cpu_count: int          # Required.
  ram: int                # Required.


# Environment settings
env:
  variables: Map          # Key-value pairs of environment variables.
  docker_image: string
  python: # Python-specific configuration.
    version: string
    pip:
      requirements_path: '<path-to-requirements.txt>'
    poetry:
      directory: '<path-to-directory-with-pyproject.toml>'
  secrets:
    variables: Map        # Secret variables.
    ssh_keys: [ ]         # SSH keys list.


# Project synchronization settings
project_sync:
  local:
    root: string          # Root directory for sync.
    storage_name: string  # Storage name.
    uri: string           # Sync URI. For DEFAULT storage set to “”
    exclude: [ string ]   # Paths to exclude. [see](https://plugins.jetbrains.com/plugin/23731-jetbrains-cadence/docs/synchronize-code.html#inclusions)
    include: [ string ]   # Paths to include.
    storage_type: string  # DEFAULT or CUSTOM.


# Download remotely before the execution (e.g., datasets, foundation models)
inputs:
  - type: INPUT
    storage_name: string  # Storage name.
    uri: string           # Path without bucket (e.g., folder/data).
    path: string          # Local path.
    acceleration: boolean
    storage_type: CUSTOM  # Inputs are not available for default storage.


# Upload remotely after the execution (e.g., models, training artifacts)
outputs:
  - type: OUTPUT
    storage_name: string  # Storage name.
    uri: string           # Path without bucket (e.g., folder/data). For default storage set to “”
    path: string          # Target path relative to the project root on a remote machine (e.g., folder/data)
    storage_type: string  # DEFAULT or CUSTOM.
```

## Resources
| GPU Type | GPUs | Provider | vRAM, GB | vCPUs | Hourly price* | Config Snippet                                                                                       |
|----------|-----:|----------|---------:|------:|--------------:|------------------------------------------------------------------------------------------------------|
| h200     |    1 | Nebius   |      200 |    16 |         $3.50 | <pre>provisioning:<br>  gpu_type: h200<br>  gpu_count: 1<br>  cpu_count: 16<br>  ram: 200</pre>      |
| h200     |    8 | Nebius   |     1600 |   128 |        $28.00 | <pre>provisioning:<br>  gpu_type: h200<br>  gpu_count: 8<br>  cpu_count: 128<br>  ram: 1600</pre>    |
| h100     |    1 | Nebius   |      160 |    20 |         $2.95 | <pre>provisioning:<br>  gpu_type: h100<br>  gpu_count: 1<br>  cpu_count: 20<br>  ram: 160</pre>      |
| h100     |    8 | Nebius   |     1280 |   160 |        $23.60 | <pre>provisioning:<br>  gpu_type: h100<br>  gpu_count: 8<br>  cpu_count: 160<br>  ram: 1280</pre>    |
| l40s     |    1 | Nebius   |       32 |     8 |         $1.55 | <pre>provisioning:<br>  gpu_type: l40s<br>  gpu_count: 1<br>  cpu_count: 8<br>  ram: 32</pre>        |
| a100-40g |    8 | AWS      |     1152 |    96 |        $32.77 | <pre>provisioning:<br>  gpu_type: a100-40g<br>  gpu_count: 8<br>  cpu_count: 96<br>  ram: 1152</pre> |
| a10g     |    1 | AWS      |      128 |    32 |         $2.45 | <pre>provisioning:<br>  gpu_type: a10g<br>  gpu_count: 1<br>  cpu_count: 32<br>  ram: 128</pre>      |
| a10g     |    4 | AWS      |      192 |    48 |         $5.67 | <pre>provisioning:<br>  gpu_type: a10g<br>  gpu_count: 4<br>  cpu_count: 48<br>  ram: 192</pre>      |
| a10g     |    8 | AWS      |      768 |   192 |        $16.29 | <pre>provisioning:<br>  gpu_type: a10g<br>  gpu_count: 8<br>  cpu_count: 192<br>  ram: 768</pre>     |
| t4       |    1 | AWS      |       64 |    16 |         $1.20 | <pre>provisioning:<br>  gpu_type: t4<br>  gpu_count: 1<br>  cpu_count: 16<br>  ram: 64</pre>         |
| t4       |    1 | AWS      |       16 |     4 |         $0.53 | <pre>provisioning:<br>  gpu_type: t4<br>  gpu_count: 1<br>  cpu_count: 4<br>  ram: 16</pre>          |
| -        |    0 | AWS      |        4 |     2 |         $0.05 | <pre>provisioning:<br>  gpu_count: 0<br>  cpu_count: 2<br>  ram: 4</pre>                             |
| -        |    0 | AWS      |       16 |     4 |         $0.17 | <pre>provisioning:<br>  gpu_count: 0<br>  cpu_count: 4<br>  ram: 16</pre>                            |
| -        |    0 | AWS      |       96 |    48 |         $1.84 | <pre>provisioning:<br>  gpu_count: 0<br>  cpu_count: 48<br>  ram: 96</pre>                           |
| -        |    0 | AWS      |     1536 |   192 |        $12.18 | <pre>provisioning:<br>  gpu_count: 0<br>  cpu_count: 192<br>  ram: 1536</pre>                        |

\* Compute billed by the minute.\
By using cloud resources of a certain provider, you are agreeing to their terms of service:
- [AWS Service Terms](https://aws.amazon.com/service-terms/)
- [Nebius Terms of Use of Compute Cloud](https://docs.nebius.com/legal/specific-terms/compute)

## Default storage

JetBrains Cadence has a built-in Cadence Storage that you can use as a default option.

Cadence Storage is an internal S3-based storage system managed by JetBrains Cadence. This storage solution ensures that
data is securely isolated, meaning that only the users with authorized access to the specific workspace can access the
data. This security mechanism guarantees that each workspace's data remains private and protected from unauthorized
access, maintaining the integrity and confidentiality of the stored information.

## Custom storage

### Add storage

You can also use your custom S3 bucket storage. To do this, you need to add a new storage via:

```shell
cadence storage add
```

Example:

```shell
> cadence storage add
Storage name: my-custom-storage
Access key ID: <access-key-id>
Secret access key: <secret-access-key>
Session token (optional):

Bucket: s3://my-custom-storage-bucket
Custom endpoint URL (optional):

Use acceleration endpoint? [y/N]:

Storage my-custom-storage added to keyring
>
> cadence storage get my-custom-storage
{
  "name": "my-custom-storage",
  "access_key_id": "<access-key-id>",
  "secret_access_key": "***",
  "profile": null,
  "session_token": "***",
  "bucket": "s3://my-custom-storage-bucket",
  "endpoint_url": null,
  "type": "CUSTOM"
}
>
```

### List storages

```shell
cadence storage list
```

## Completions

Cadence CLI uses click for its command line interface. click can automatically generate completion files for bash, fish,
and zsh which can either be generated and sourced each time your shell is started or, generated once, save to a file and
sourced from there. The latter version is much more efficient.

To enable shell completions:

### bash

```bash
echo 'eval "$(_CADENCE_COMPLETE=bash_source cadence)"' >> ~/.bashrc
```

### zsh

```zsh
echo 'eval "$(_CADENCE_COMPLETE=zsh_source cadence)"' >> ~/.zshrc
```

### fish

```shell
echo 'eval (env _KHAL_COMPLETE=fish_source khal)"' >> ~/.config/fish/completions/khal.fish
```

---
