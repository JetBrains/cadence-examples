## Config file format:

```yaml
working_dir: string       # Required.
cmd:                      # Commands to run in sequence. Required.
  - string
description: string


# Provisioning configuration Required.
# Must be one of the available resources,
# see https://plugins.jetbrains.com/plugin/23731-jetbrains-cadence/docs/resources.html
provisioning:
  gpu_type: string | null # Required.
  gpu_count: int | null   # Required.
  cpu_count: int          # Required.
  ram: int                # Required.


# Environment settings
env:
  variables: Map          # Key-value pairs of environment variables.
  docker_image: string
  python:                 # Python-specific configuration.
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
## Examples
- [Basic example](examples/basic) - Simple example that only uses default storage.
- [Llama fine-tuning example](examples/llama-fine-tuning) - Example demonstrating how to fine-tune the Mistral-7B language model using LoRA.
- [Complex example](examples/complex) - Advanced example with custom storage and more complex configuration.

## Custom storage

### Add storage

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
