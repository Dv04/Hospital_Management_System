from functools import wraps
import os
from urllib import request

from flask import Flask, render_template, redirect, url_for, request, flash, session

from flask_bootstrap import Bootstrap
import requests
from forms import (
    DiseaseDetailsForm,
    PatientDetailsForm,
    LoginUserForm,
    RegisterUserForm,
    STTForm,
)
from werkzeug.security import generate_password_hash, check_password_hash

from speechToText import convert_speech_to_text
from predict_disease import predict_disease

from backend.mongoConnect import *
from model import *

from flask import Flask, request, jsonify
from PIL import Image
import io


app = Flask(__name__, static_folder="static")
Bootstrap(app=app)
app.app_context().push()
app.secret_key = "secret-tunnel"


class User:
    email = ""
    role = ""
    is_active = False


def logged_in(function):
    @wraps(function)
    def decorated_function(*args, **kwargs):
        if user.is_active:
            return function(*args, **kwargs)
        else:
            return redirect(url_for("login_page"))

    return decorated_function

user = User()


@app.route("/")
def home_page():
    return render_template("index.html", logged_in=logged_in, user=user)


@app.route("/about")
def about_page():
    return render_template("about.html")


@app.route("/login", methods=["GET", "POST"])
def login_page():
    user_login = LoginUserForm()
    if user_login.validate_on_submit():
        email = user_login.email.data
        role = user_login.role.data
        emailCheck = db["users"].find_one({"email": email})
        if emailCheck:
            hashPassword = emailCheck["password"]

            password = user_login.password.data

            if email == emailCheck["email"] and role == emailCheck["role"]:
                if check_password_hash(pwhash=hashPassword, password=password):
                    user.email = email
                    user.role = role
                    user.is_active = True
                    session['user'] = {  # Store user data in a session
                        'email': email,
                        'role': role,
                        'is_active': True
                    }
                    print("Log in successful")
                    return redirect(url_for(f"{role}_page"))

            else:
                print("User does not exist")
                return redirect(url_for("register_page"))

        else:
            flash("This Email is not registered. Please try again!")
            print("Wrong Email")
            return redirect(url_for("login_page"))
    return render_template("login.html", login_form=user_login, user=user)


@app.route("/register", methods=["GET", "POST"])
def register_page():
    register_form = RegisterUserForm()
    if register_form.validate_on_submit():
        email = register_form.email.data
        name = register_form.name.data
        password = generate_password_hash(
            register_form.password.data, method="pbkdf2:sha256", salt_length=8
        )
        role = register_form.role.data
        phone_no = register_form.phone_no.data
        gender = register_form.gender.data
        address = register_form.address.data

        user.email = email
        user.role = role
        user.is_active = True

        data = {
            "role": role,
            "email": email,
            "name": name,
            "password": password,
            "phone_no": phone_no,
            "gender": gender,
            "address": address,
        }

        if request.method == "POST":
            emailCheck = db["users"].find_one({"email": email})
            print("Email cehck:", emailCheck)

            if emailCheck:
                print("Email already exists")
                return redirect(url_for("register_page"))

            result = insert("users", data)

            if result:
                print("Inserted Successfully")
                print(result)
                return redirect(url_for(f"home_page", user=user))
            else:
                print("Insertion Failed")
                print(result)

        return redirect(url_for(f"{role}_page", user=user))
    return render_template("register.html", register_form=register_form, user=user)


@app.route("/sign-out")
@logged_in
def sign_out_page():
    user.email = ""
    user.role = ""
    user.is_active = False
    return redirect(url_for("home_page"))


@app.route("/staff", methods=["GET", "POST"])
@logged_in
def staff_page():
    data = None
    if request.method == 'GET':
        data = find("doctors")
    return render_template("staff.html", user=user, staff_data=data)


@app.route("/medicine", methods=["GET", "POST"])
@logged_in
def hospital_page():
    data = None
    if request.method == 'GET':
        data = find("madicine")
    return render_template("medicine.html", user=user, medicine_data=data)


@app.route("/doctor", methods=["GET", "POST"])
@logged_in
def doctor_page():
    stt_form = STTForm()
    text = None
    if stt_form.validate_on_submit():
        text = convert_speech_to_text("recorded/recorded-audio.wav")
    return render_template("doctor.html", user=user, stt_form=stt_form, text=text)


@app.route("/reception", methods=["GET", "POST"])
def reception_page():
    stt_form = STTForm()
    return redirect(url_for("disease_prediction"))

@app.route("/prediction", methods=["GET", "POST"])
@logged_in
def disease_prediction():
    form = DiseaseDetailsForm(request.form)
    if request.method == "POST":
        print("Form:", request.form)
        print("Form Submitted")
        # if form.validate_on_submit():

        selected_symptoms = request.form.getlist(
            "symptomp_list"
        )  # Use getlist to handle multiple selections
        print(selected_symptoms)
        input_symptoms_str = ",".join(selected_symptoms)
        result = predict_disease(input_symptoms_str)

        unique_values = set()

        # Iterate through the values of the dictionary and add them to the set
        for value in result.values():
            unique_values.add(value)

        # If the set contains only one value, then the prediction is successful
        if len(unique_values) >= 1:
            print(unique_values)
        else:
            print("Prediction Failed")
            result = "Prediction Failed"
        return render_template(
            "prediction.html", form=form, result=unique_values, user=user
        )
        # else:
        #     print("Form Validation Failed")  # Debugging message

    return render_template("prediction.html", form=form, user=user)


@app.route("/patient", methods=["GET", "POST"])
@logged_in
def patient_page():
    if request.method == 'GET':
        data = find("patient")
        return render_template("patient.html", user=user, patient_data=data)



@app.route("/pharmacy")
@logged_in
def pharmacy_page():
    return render_template("pharmacy.html", user=user)


@app.route("/camera")
@logged_in
def camera_page():
    return render_template("camera.html", user=user)


@app.route("/about-us")
def about_us_page():
    return render_template("about.html", user=user)


@app.route("/not_found")
@app.errorhandler(404)
def not_found(e):
    return render_template("not_found.html")

@app.route("/process_image", methods=["POST"])
def process_image():
    print("Processing image")
    try:
        uploaded_file = request.files["image"]
        if uploaded_file.filename != "":
            image_path = os.path.join("uploads", uploaded_file.filename)
            uploaded_file.save(image_path)
            
            extracted_text = ocr_core(image_path)  # Use the OCR function
            response = {"text": extracted_text}

            data = insert("prescription", {"text": extracted_text})

            if data:
                print("Inserted Successfully")
                print(data)

            else: 
                print("Insertion Failed")
                print(data)
        else:
            response = {"error": "No file uploaded"}
    except Exception as e:
        response = {"error": str(e)}
    
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)
