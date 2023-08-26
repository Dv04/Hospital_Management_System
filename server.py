import os
from urllib import request
from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
import requests
from forms import DiseaseDetailsForm, PatientDetailsForm, LoginUserForm, RegisterUserForm, STTForm
from werkzeug.security import generate_password_hash, check_password_hash
from speechToText import convert_speech_to_text
from flask import Flask, request, jsonify
from PIL import Image
import io

app = Flask(__name__, static_folder='static')
Bootstrap(app=app)
app.app_context().push()
app.secret_key = "secret-tunnel"

class User:
    email = ""
    role = ""
    is_active = False

logged_in = False
user = User()

@app.route('/')
def home_page():
    return render_template('index.html', logged_in=logged_in, user=user)

@app.route('/about')
def about_page():
    return render_template('about.html')

@app.route('/login', methods=["GET", "POST"])
def login_page():
    user_login = LoginUserForm()
    if user_login.validate_on_submit():
        email = user_login.email.data
        role = user.role.data
        if email == "Get the email in database" and role == "Get the role in database":
            hashed_password = "Get the hashed password for the email"
            password = check_password_hash(
                pwhash= hashed_password,
                password=user_login.password.data
            )

            user.email = email
            user.role = role
            user.is_active = True
            return redirect(url_for(f"{role}_page"), user=user)
    return render_template('login.html', login_form=user_login, user=user)

@app.route('/register', methods=["GET", "POST"])
def register_page():
    register_form = RegisterUserForm()
    if register_form.validate_on_submit():
        email = register_form.email.data
        name = register_form.name.data
        password = generate_password_hash(
            register_form.password.data,
            method='pbkdf2:sha256',
            salt_length=8
        )
        role = register_form.role.data
        phone_no = register_form.phone_no.data
        gender = register_form.gender.data
        address = register_form.address.data

        user.email = email
        user.role = role
        user.is_active = True

        print(email)
        print(name)
        print(password)
        print(role)
        print(phone_no)
        print(gender)
        print(address)

        return redirect(url_for(f"{role}_page", user=user))
    return render_template('register.html', register_form=register_form, user=user)

@app.route('/staff')
def staff_page():
    return render_template('staff.html', user=user)

@app.route('/reception')
def hospital_page():
    return render_template('reception.html', user=user)

@app.route('/doctor', methods=["GET", "POST"])
def doctor_page():
    stt_form = STTForm()
    text=None
    if stt_form.validate_on_submit():
        text = convert_speech_to_text('recorded/recorded-audio.wav')
    return render_template('doctor.html', user=user, stt_form=stt_form, text=text)

@app.route('/patient')
def patient_page():
    return render_template('patient.html', user=user)

@app.route('/pharmacy')
def pharmacy_page():
    return render_template('pharmacy.html', user=user)

@app.route('/camera')
def camera_page():
    return render_template('camera.html', user=user)

@app.route('/process_image', methods=['POST'])
def process_image():
    data = request.json
    image_data = data['image'].split(',')[1]  # Extract image data from base64 format

    # You can save the image data as a file here if needed
    # For now, we'll just return a sample text
    sample_text = "Hello, World!"

    return jsonify({'text': sample_text})

@app.route('/not_found')
@app.errorhandler(404)
def not_found(e):
    return render_template('not_found.html')

if __name__ == "__main__":
    app.run(debug=True)
