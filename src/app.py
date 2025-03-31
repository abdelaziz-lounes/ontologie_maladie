import streamlit as st
import json
import re

# Set the page configuration (must be the first Streamlit command)
st.set_page_config(page_title="Medical Ontology Search", page_icon="🩺", layout="wide")

# Load the medical data from the JSON file
with open("src/data/medical_data.json", "r", encoding="utf-8") as file:
    medical_data = json.load(file)

# Inject custom CSS for font size
st.markdown(
    """
    <style>
    /* Increase the font size for the entire app */
    body {
        font-size: 24px;
    }
    /* Customize headers */
    h1 {
        font-size: 36px;
    }
    h2 {
        font-size: 30px;
    }
    h3 {
        font-size: 24px;
    }
    .box {
        border: 1px solid #ccc;
        border-radius: 8px;
        padding: 16px;
        margin-bottom: 16px;
    }
    .box h4 {
        margin-top: 0;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ================================
# ⚡ Search Functionality
# ================================
def search_medical_data(query):
    """Analyze the query and return matching diseases, symptoms, or treatments."""
    query = query.lower()
    results = []

    # Check if the query asks for symptoms of a specific disease
    match = re.search(r"symptoms associated with (.+)", query)
    if match:
        disease_name = match.group(1).strip()
        for entry in medical_data:
            disease = entry["disease"]
            if disease_name == disease["name"].lower():
                return [disease]  # Return the full disease object
        return []

    # Check if the query asks for treatments for a specific disease
    match = re.search(r"treatments are available for (.+)", query)
    if match:
        disease_name = match.group(1).strip()
        for entry in medical_data:
            disease = entry["disease"]
            if disease_name == disease["name"].lower():
                return [disease]  # Return the full disease object
        return []

    # Check if the query asks for diseases treated by a specific treatment
    match = re.search(r"diseases are treated by (.+)", query)
    if match:
        treatment_name = match.group(1).strip()
        for entry in medical_data:
            disease = entry["disease"]
            if treatment_name in [t.lower() for t in disease.get("treatments", [])]:
                results.append(disease)
        return results

    # Check if the query asks for diseases with a specific symptom
    match = re.search(r"diseases have the symptom (.+)", query)
    if match:
        symptom_name = match.group(1).strip()
        for entry in medical_data:
            disease = entry["disease"]
            if symptom_name in [s.lower() for s in disease.get("symptoms", [])]:
                results.append(disease)
        return results

    # Check if the query asks for treatments for diseases with a specific symptom
    match = re.search(r"treatments for diseases associated with (.+)", query)
    if match:
        symptom_name = match.group(1).strip()
        for entry in medical_data:
            disease = entry["disease"]
            if symptom_name in [s.lower() for s in disease.get("symptoms", [])]:
                return [disease]  # Return the full disease object
        return []

    # Fallback: General search for diseases by name or description
    for entry in medical_data:
        disease = entry["disease"]
        if query in disease["name"].lower() or query in disease["description"].lower():
            results.append(disease)

    return results

# ================================
# 🎨 Streamlit Interface
# ================================
# Header
st.title("🩺 Medical Ontology Search")
st.write("Search for diseases, symptoms, or treatments in the medical ontology.")

# Input field for the query
query = st.text_input("🔍 Enter your query (e.g., 'Diabetes', 'Fever', 'Insulin therapy')")

# Perform the search if a query is entered
if query:
    results = search_medical_data(query)

    if results:
        st.write(f"### 📋 Results for '{query}':")
        for result in results:
            # Check if the result contains only treatments or symptoms
            if "treatments" in result and "name" not in result:
                st.markdown("### 💊 Treatments")
                st.write("Here are the treatments available:")
                st.markdown(", ".join([f"`{treatment}`" for treatment in result["treatments"]]))
            elif "symptoms" in result and "name" not in result:
                st.markdown("### 🩺 Symptoms")
                st.write("Here are the symptoms associated:")
                st.markdown(", ".join([f"`{symptom}`" for symptom in result["symptoms"]]))
            else:
                # Assume the result is a disease object
                disease = result

                st.markdown(f"### 🦠 Disease: {disease.get('name', 'Unknown')}")

                # Description Section
                st.markdown(
                    f"""
                    <div class="box">
                        <h4>📝 Description</h4>
                        <p>{disease.get('description', 'No description available')}</p>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

                # Symptoms Section
                st.markdown(
                    f"""
                    <div class="box">
                        <h4>🩺 Symptoms</h4>
                        <p>{", ".join([f"`{symptom}`" for symptom in disease.get("symptoms", [])])}</p>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

                # Treatments Section
                st.markdown(
                    f"""
                    <div class="box">
                        <h4>💊 Treatments</h4>
                        <p>{", ".join([f"`{treatment}`" for treatment in disease.get("treatments", [])])}</p>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

                # Links Section
                with st.expander("🔗 Learn more"):
                    for link in disease.get("links", []):
                        st.markdown(f"- [Link]({link})")

                # Add a separator for better readability
                st.write("---")
    else:
        st.warning("❌ No results found for your query.")