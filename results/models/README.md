# Models Directory

## Overview
This directory stores the trained models and their associated files. These include final models ready for deployment, intermediate model checkpoints, and model architecture definitions.

## Contents
- **Model Checkpoints:** Intermediate model states saved during training when the model achieves a new peak in performance.
- **Final Models:** The trained models saved after the completion of the training process. These are ready for inference or deployment.
- **Model Architectures:** Separate files containing model architecture definitions, often in JSON or YAML format, especially for complex custom models.

## Naming Convention
Model files are named following the scheme:
`<model_type>_<feature_descriptor>_<date>.<extension>`
For example, `deep_neural_network_genomic_data_20230409.h5`.

## Usage
To load a model, refer to the specific instructions provided in the main project README, as the process may vary depending on the model type and the library used.

## Note
For large model files, consider using Git LFS or DVC to manage storage and versioning efficiently.
