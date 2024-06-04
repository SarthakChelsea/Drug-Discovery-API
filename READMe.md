# Bioinformatics Project - Sarthak Mahapatra

This repository contains the source code for building a machine learning model using ChEMBL bioactivity data. The project is implemented in a single Jupyter notebook, `Model_training.ipynb`, which covers all aspects of the data processing and model development pipeline.

## Project Overview

The project is divided into five main parts, all of which are included in the `Model_training.ipynb` notebook:

1. **Part 1: Data Collection and Pre-Processing**
    - Collect data from the ChEMBL database.
    - Pre-process the data to prepare it for descriptor calculation and model building.

2. **Part 2: Lipinski Descriptor Calculation**
    - Calculate Lipinski descriptors, which are important for assessing the drug-likeness of compounds.

3. **Part 3: Padel Molecular Descriptors Calculation**
    - Calculate Padel molecular descriptors, which provide a quantitative description of the compounds in the dataset.
    - Prepare the dataset for subsequent model building.

4. **Part 4: Model Building and Feature Reduction**
    - Compare several machine learning algorithms and feature reduction methods.
    - Build regression models for predicting the activity of acetylcholinesterase inhibitors.

5. **Part 5: Model Deployment**
    - Use the best model to create an sklearn pipeline.
    - The pipeline takes input as canonical SMILES, performs feature extraction, PCA, regression, and outputs IC50 values.
    - Save the model as a pickle file and create an API using FastAPI for easy access and integration.

## Getting Started

### Prerequisites

- Python 3.x
- Jupyter Notebook
- pip (Python package installer)

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/SarthakChelsea/Drug-Discovery-API.git
    cd bioinformatics-project
    ```

2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

### Usage

1. Launch Jupyter Notebook:
    ```bash
    jupyter notebook
    ```

2. Open the `Model_training.ipynb` notebook and run the cells sequentially to execute the project.


## Acknowledgements

- ChEMBL database for providing the bioactivity data.
- Padel-Descriptor software for calculating molecular descriptors.

---

For any questions or issues, please contact [Sarthak Mahapatra](mailto:sarthakchelsea@gmail.com).
