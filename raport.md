### **Rapport du Projet d'Ontologie Médicale**

---

### **Introduction**
Le **Projet d'Ontologie Médicale** est conçu pour organiser et représenter les connaissances médicales de manière structurée et lisible par les machines. Il utilise **OWL (Web Ontology Language)** pour définir les relations entre les maladies, les symptômes et les traitements. Cette ontologie peut être interrogée de manière interactive via une application basée sur Streamlit, facilitant ainsi l'exploration des données médicales.

---

### **Qu'est-ce qu'une Ontologie ?**
Une **ontologie** est une manière structurée de représenter des connaissances. Elle définit :
- **Classes** : Catégories de choses (par exemple, maladies, symptômes, traitements).
- **Propriétés** : Relations entre ces catégories (par exemple, une maladie a des symptômes, une maladie est traitée par des traitements).
- **Individus** : Exemples spécifiques de ces catégories (par exemple, le diabète est un individu de la classe Maladie).

Dans ce projet :
- **Les maladies** comme le diabète et le paludisme sont représentées comme des individus de la classe `Disease`.
- **Les symptômes** comme la fièvre et la vision floue sont des individus de la classe `Symptom`.
- **Les traitements** comme l'insulinothérapie et les médicaments antipaludiques sont des individus de la classe `Treatment`.

---

### **Structure du Projet**
Le projet est organisé comme suit :

#### **1. Code Source (src)**
- **`app.py`** : Une application Streamlit pour interroger l'ontologie de manière interactive.
- **`ontology_builder.py`** : Un script pour construire l'ontologie à partir des données médicales.
- **`utils/helpers.py`** : Contient des fonctions utilitaires pour charger, valider et transformer les données médicales.

#### **2. Données (data)**
- **`medical_data.json`** : Un fichier JSON contenant les données médicales, y compris les maladies, les symptômes et les traitements.

#### **3. Ontologie (ontology)**
- **`medical_ontology.owl`** : Le fichier OWL qui représente l'ontologie médicale.

#### **4. Documentation**
- **`README.md`** : Fournit un aperçu du projet et des instructions pour l'installation et l'utilisation.

---

### **Comment Fonctionne l'Ontologie**
L'ontologie est construite en utilisant **OWL** et définit les éléments suivants :

#### **1. Classes**
- **`Disease`** : Représente les maladies (par exemple, Diabète, Paludisme).
- **`Symptom`** : Représente les symptômes (par exemple, Fièvre, Vision floue).
- **`Treatment`** : Représente les traitements (par exemple, Insulinothérapie, Médicaments antipaludiques).
- **`Patient`** : Représente les patients (peu utilisé dans ce projet).

#### **2. Propriétés**
- **`hasSymptom`** : Lie une maladie à ses symptômes.
  - Exemple : Le paludisme **hasSymptom** Fièvre.
- **`treatedBy`** : Lie une maladie à ses traitements.
  - Exemple : Le paludisme **treatedBy** Médicaments antipaludiques.
- **`hasName`** : Stocke le nom d'une maladie, d'un symptôme ou d'un traitement.
- **`hasDescription`** : Stocke une description d'une maladie.

#### **3. Individus**
- **Maladies** : Diabète, Paludisme, Hypertension, etc.
- **Symptômes** : Fièvre, Vision floue, etc.
- **Traitements** : Insulinothérapie, Médicaments antipaludiques, etc.

---

### **Comment l'Ontologie est Construite**
L'ontologie est créée à l'aide du script `ontology_builder.py`. Voici les étapes :

1. **Chargement des Données Médicales** :
   - Le script lit le fichier `medical_data.json`, qui contient des informations sur les maladies, les symptômes et les traitements.

2. **Définition des Classes et Propriétés** :
   - Le script définit les classes (`Disease`, `Symptom`, `Treatment`) et les propriétés (`hasSymptom`, `treatedBy`, etc.) dans l'ontologie.

3. **Création des Individus** :
   - Pour chaque maladie dans le fichier JSON, le script crée un individu dans l'ontologie.
   - Il crée également des individus pour les symptômes et les traitements de chaque maladie et les relie à l'aide des propriétés.

4. **Sauvegarde de l'Ontologie** :
   - L'ontologie est sauvegardée sous forme de fichier OWL (`medical_ontology.owl`) dans le dossier ontology.

---

### **Exemple d'Ontologie en OWL**
Voici un exemple simplifié de l'ontologie en OWL :

```xml
<owl:Class rdf:about="#Disease"/>
<owl:Class rdf:about="#Symptom"/>
<owl:Class rdf:about="#Treatment"/>

<owl:ObjectProperty rdf:about="#hasSymptom">
  <rdfs:domain rdf:resource="#Disease"/>
  <rdfs:range rdf:resource="#Symptom"/>
</owl:ObjectProperty>

<owl:ObjectProperty rdf:about="#treatedBy">
  <rdfs:domain rdf:resource="#Disease"/>
  <rdfs:range rdf:resource="#Treatment"/>
</owl:ObjectProperty>

<owl:NamedIndividual rdf:about="#Diabetes">
  <rdf:type rdf:resource="#Disease"/>
</owl:NamedIndividual>

<owl:NamedIndividual rdf:about="#Fever">
  <rdf:type rdf:resource="#Symptom"/>
</owl:NamedIndividual>

<owl:NamedIndividual rdf:about="#InsulinTherapy">
  <rdf:type rdf:resource="#Treatment"/>
</owl:NamedIndividual>
```

---

### **Comment Fonctionne l'Application Streamlit**
Le fichier `app.py` crée une interface conviviale pour interroger l'ontologie. Voici comment il fonctionne :

#### **1. Fonctionnalité de Recherche**
- Les utilisateurs peuvent taper des requêtes comme :
  - "Quels sont les symptômes du diabète ?"
  - "Quels traitements sont disponibles pour le paludisme ?"
- L'application traite la requête et recherche dans l'ontologie les résultats correspondants.

#### **2. Affichage des Résultats**
- L'application affiche les résultats dans un format clair, montrant :
  - Le nom et la description de la maladie.
  - Les symptômes et les traitements.
  - Des liens pour plus d'informations.

#### **3. Fonctionnalités Interactives**
- L'application utilise des sections repliables (`st.expander`) et des onglets (`st.tabs`) pour organiser les résultats.

---

### **Exemples de Requêtes**
Voici quelques exemples de requêtes et leurs résultats :

#### Requête : "Quels sont les symptômes du diabète ?"
**Résultat** :
- **Maladie** : Diabète
- **Symptômes** : Soif excessive, Mictions fréquentes, Fatigue extrême, Vision floue

#### Requête : "Quels traitements sont disponibles pour le paludisme ?"
**Résultat** :
- **Maladie** : Paludisme
- **Traitements** : Médicaments antipaludiques, Mesures préventives, Soins de soutien

---

### **Pourquoi Cette Ontologie est Utile**
1. **Connaissances Organisées** :
   - L'ontologie organise les connaissances médicales de manière structurée, facilitant leur recherche et leur compréhension.

2. **Interopérabilité** :
   - Le format OWL permet à l'ontologie d'être utilisée dans d'autres systèmes et applications.

3. **Évolutivité** :
   - De nouvelles maladies, symptômes et traitements peuvent être ajoutés facilement en mettant à jour le fichier JSON.

---

### **Améliorations Futures**
1. **Étendre l'Ontologie** :
   - Ajouter davantage de maladies, symptômes et traitements pour rendre l'ontologie plus complète.

2. **Traitement du Langage Naturel (NLP)** :
   - Améliorer la capacité de l'application à comprendre des requêtes complexes en utilisant des techniques de NLP.

3. **Visualisation** :
   - Ajouter des représentations graphiques des relations entre les maladies, les symptômes et les traitements.

---

### **Conclusion**
Ce projet démontre comment une ontologie peut être utilisée pour organiser et représenter les connaissances médicales. En combinant OWL pour la représentation sémantique et Streamlit pour l'interaction utilisateur, le projet fournit un outil puissant pour explorer les informations médicales.

--- 