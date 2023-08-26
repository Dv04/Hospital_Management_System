import numpy as np
import pandas as pd
from scipy.stats import mode
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

# Load and preprocess the dataset
DATA_PATH = "dataset/Training.csv"
data = pd.read_csv(DATA_PATH).dropna(axis=1)
encoder = LabelEncoder()
data["prognosis"] = encoder.fit_transform(data["prognosis"])

# Generating symptom index
symptoms = data.columns[:-1]
symptom_index = {symptom: index for index, symptom in enumerate(symptoms)}

# Generating predictions classes
predictions_classes = encoder.classes_

# Save symptom index and predictions classes using joblib
data_dict = {
    "symptom_index": symptom_index,
    "predictions_classes": predictions_classes
}
joblib.dump(data_dict, 'models/data_dict.pkl')

X = data.iloc[:, :-1]
y = data.iloc[:, -1]

# Train models
svm_model = SVC()
svm_model.fit(X, y)

nb_model = GaussianNB()
nb_model.fit(X, y)

rf_model = RandomForestClassifier(random_state=18)
rf_model.fit(X, y)

# Save trained models using joblib
joblib.dump(svm_model, 'models/svm_model.pkl')
joblib.dump(nb_model, 'models/nb_model.pkl')
joblib.dump(rf_model, 'models/rf_model.pkl')

print("Models trained and saved successfully.")
