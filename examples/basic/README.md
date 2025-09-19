# Basic Example

This example demonstrates how to run a simple Python script using Cadence. It shows the basic configuration for provisioning resources, setting up a Python environment, and saving outputs.

## How to run

Navigate to the `basic` directory and run the following command:

```bash
cadence execution start --preset basic_preset.yaml
```

This will provision the required resources (2 CPUs and 4GB RAM), set up the Python environment, and execute the script that prints the torch version and saves a text file to the outputs directory.
