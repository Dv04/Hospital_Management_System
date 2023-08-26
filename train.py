from predict_disease import predict_disease

input_symptoms = ["blister", "red_sore_around_nose", "yellow_crust_ooze"]
input_symptoms_str = ",".join(input_symptoms)

result = predict_disease(input_symptoms_str)
print(result)
