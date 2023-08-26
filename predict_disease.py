import numpy as np
import pandas as pd
from scipy.stats import mode
from sklearn.preprocessing import LabelEncoder
import joblib

# Load symptom index and predictions classes
data_dict = joblib.load("models/data_dict.pkl")

# Load trained models
svm_model = joblib.load("models/svm_model.pkl")
nb_model = joblib.load("models/nb_model.pkl")
rf_model = joblib.load("models/rf_model.pkl")


# Define the function to predict diseases
def predict_disease(symptoms):
    symptoms = symptoms.split(",")

    input_data = [0] * len(data_dict["symptom_index"])
    for symptom in symptoms:
        index = data_dict["symptom_index"][symptom]
        input_data[index] = 1

    input_data = np.array(input_data).reshape(1, -1)

    rf_prediction = data_dict["predictions_classes"][rf_model.predict(input_data)[0]]
    nb_prediction = data_dict["predictions_classes"][nb_model.predict(input_data)[0]]
    svm_prediction = data_dict["predictions_classes"][svm_model.predict(input_data)[0]]

    final_prediction = mode([rf_prediction, nb_prediction, svm_prediction])[0][0]
    predictions = {
        "rf_model_prediction": rf_prediction,
        "naive_bayes_prediction": nb_prediction,
        "svm_model_prediction": svm_prediction,
        "final_prediction": final_prediction,
    }
    return predictions


if __name__ == "__main__":
    input_symptoms = ["blister","red_sore_around_nose", "yellow_crust_ooze"]
    input_symptoms_str = ",".join(input_symptoms)
    result = predict_disease(input_symptoms_str)
    print(result)
