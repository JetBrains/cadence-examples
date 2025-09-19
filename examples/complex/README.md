# Complex Example

This example demonstrates advanced features of Cadence for running multi-step machine learning workflows. It showcases custom storage configuration, file inclusion/exclusion patterns, environment variables and secrets management, Poetry for dependency management, and sophisticated input/output handling.

## How to run

Navigate to the `complex` directory.

Add custom storage named `my-custom-storage` by running:
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
```

Run the following command:

```bash
cadence execution start --preset complex_preset.yaml
```

This will provision the required resources (H200 GPU), set up the environment using Poetry, download the necessary input files from storage, execute the training and testing scripts in sequence, and save the outputs to the configured storage locations.