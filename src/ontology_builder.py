from owlready2 import *
import json
import os

# Load the medical data from the JSON file
with open("src/data/medical_data.json", "r", encoding="utf-8") as file:
    medical_data = json.load(file)

# Create a new ontology
onto = get_ontology("http://example.org/medical.owl")

with onto:
    # Define classes for diseases, symptoms, treatments, and other entities
    class Disease(Thing): pass
    class Symptom(Thing): pass
    class Treatment(Thing): pass
    class Patient(Thing): pass

    # Define properties
    class hasSymptom(Disease >> Symptom, ObjectProperty): pass
    class treatedBy(Disease >> Treatment, ObjectProperty): pass
    class hasPatient(Treatment >> Patient, ObjectProperty): pass
    class hasName(Thing >> str, DataProperty, FunctionalProperty): pass
    class hasDescription(Thing >> str, DataProperty, FunctionalProperty): pass

    # Create instances based on the medical data
    for entry in medical_data:  # Iterate over the list directly
        disease = entry["disease"]
        disease_name = disease.get("name", None)
        if not disease_name:
            print("Skipping entry with missing disease name.")
            continue

        # Create a Disease instance
        try:
            disease_instance = Disease(disease_name)
            if "description" in disease:
                disease_instance.hasDescription.append(disease["description"])
        except Exception as e:
            print(f"Error creating Disease instance for {disease_name}: {e}")
            continue

        # Create Symptom instances and link them to the Disease
        for symptom in disease.get("symptoms", []):
            try:
                symptom_instance = Symptom(symptom)
                disease_instance.hasSymptom.append(symptom_instance)
            except Exception as e:
                print(f"Error creating Symptom instance for {symptom}: {e}")

        # Create Treatment instances and link them to the Disease
        for treatment in disease.get("treatments", []):
            try:
                treatment_instance = Treatment(treatment)
                disease_instance.treatedBy.append(treatment_instance)
            except Exception as e:
                print(f"Error creating Treatment instance for {treatment}: {e}")

# Ensure the ontology directory exists
os.makedirs("ontology", exist_ok=True)

# Save the ontology to an OWL file
try:
    onto.save(file="ontology/medical_ontology.owl", format="rdfxml")
    print("Ontology saved as medical_ontology.owl")
except Exception as e:
    print(f"Error saving ontology: {e}")