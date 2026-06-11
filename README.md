# HealthWise - Disease Prediction System

## Overview
HealthWise is a machine learning-based disease prediction system that allows users to input symptoms and receive predictions about possible diseases. It provides symptom descriptions and recommended precautions to help users take appropriate action.

## Features
- Predicts diseases based on user-input symptoms.
- Provides a detailed description of predicted diseases.
- Suggests precautions for the predicted diseases.
- Uses a trained Random Forest model for predictions.
- Built using **Streamlit** for an interactive and user-friendly web interface.

## Installation & Setup
### Prerequisites
Ensure you have Python installed along with the required libraries:
```bash
pip install -r requirements.txt
```

### Running the Application
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd HealthWise
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Create and copy `config.toml` file into your device's Streamlit folder to ensure smooth execution.
4. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

## File Structure
```
HealthWise/
│-- app.py                   # Main application file
│-- train_model.py           # Script to train the ML model
│-- dataset.csv              # Dataset used for training
│-- disease_prediction_model.pkl  # Pretrained model
│-- pages/                   # Additional Streamlit pages
│-- .devcontainer/           # DevContainer configuration
│-- symptom_Description.csv  # Descriptions of symptoms
│-- symptom_precaution.csv   # Precautionary measures for diseases
│-- Symptom-severity.csv     # Severity levels of symptoms
│-- requirements.txt         # Dependencies for the project
```

## Model Details
- The disease prediction model is built using **Random Forest**.
- The model is trained using labeled symptom data from `dataset.csv`.
- The trained model is saved as `disease_prediction_model.pkl`. 

