# Medical Ontology Project

This project aims to transform medical data into an OWL ontology for semantic representation. The ontology will facilitate better understanding and interoperability of medical concepts, including diseases, symptoms, treatments, and other relevant entities.

## Project Structure

- **src/**: Contains the source code for building the ontology.
  - **ontology_builder.py**: Responsible for building the OWL ontology from the medical data. It loads the JSON data, defines the ontology structure, and creates classes and properties based on the medical concepts.
  - **data/**: Contains the medical data in JSON format.
    - **medical_data.json**: Includes information about diseases, symptoms, treatments, and other relevant medical entities.
  - **utils/**: Contains utility functions that assist in processing the medical data and constructing the ontology.
    - **helpers.py**: Exports functions for data validation, transformation, and logging.

- **ontology/**: Contains the generated OWL ontology.
  - **medical_ontology.owl**: Represents the medical data semantically, including classes, properties, and instances based on the input data.

- **requirements.txt**: Lists the dependencies required for the project, such as `owlready2` for ontology manipulation and any other libraries needed for data processing.

- **.gitignore**: Specifies files and directories that should be ignored by version control, such as compiled files and temporary data.

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd medical-ontology-project
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Prepare your medical data in the `src/data/medical_data.json` file.

4. Run the ontology builder:
   ```
   python src/ontology_builder.py
   ```

5. The generated OWL ontology will be saved in the `ontology/medical_ontology.owl` file.

## Overview of the Ontology Structure

The ontology will include:
- Classes representing medical concepts such as Diseases, Symptoms, and Treatments.
- Properties that define relationships between these concepts.
- Instances that represent specific examples of these concepts based on the input data.

For further details on the ontology structure and its usage, please refer to the documentation within the code.