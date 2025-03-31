import json

def load_medical_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def validate_medical_data(data):
    required_fields = ['disease', 'symptoms', 'treatments']
    for entry in data:
        for field in required_fields:
            if field not in entry:
                raise ValueError(f"Missing required field: {field} in entry {entry}")

def transform_data_for_ontology(data):
    transformed_data = []
    for entry in data:
        transformed_entry = {
            'disease': entry['disease'],
            'symptoms': entry.get('symptoms', []),
            'treatments': entry.get('treatments', [])
        }
        transformed_data.append(transformed_entry)
    return transformed_data

def log_message(message):
    print(f"[LOG] {message}")