
from functools import wraps
import os
from urllib import request

from flask import Flask, render_template, redirect, url_for, request, flash

from flask_bootstrap import Bootstrap
import requests
from forms import DiseaseDetailsForm, PatientDetailsForm, LoginUserForm, RegisterUserForm, STTForm
from werkzeug.security import generate_password_hash, check_password_hash

from speechToText import convert_speech_to_text


from backend.mongoConnect import *


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

def logged_in(function):
    @wraps(function)
    def decorated_function(*args, **kwargs):
        if user.is_active:
            return function(*args, **kwargs)
        else:
            return redirect(url_for('login_page'))
    return decorated_function

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
        role = user_login.role.data
        emailCheck = db['users'].find_one({'email' : email})
        if(emailCheck):
            hashPassword = emailCheck['password']
            
            password = generate_password_hash(
                            user_login.password.data,
                            method='pbkdf2:sha256',
                            salt_length=8
                        )
            
            if email == emailCheck['email'] and role == emailCheck['role']:
                password = check_password_hash(
                    pwhash=hashPassword,
                    password=password
                )

                user.email = email
                user.role = role
                user.is_active = True
                print("Log in successful")
                return redirect(url_for(f"{role}_page", user=user))
            
            else:
                print("User does not exist")
                return redirect(url_for('register_page'))
            
        else:
            flash("This Email is not registered. Please try again!")
            print("Wrong Email")
            return redirect(url_for('login_page'))
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

        data = {
            "role": role,
            "email": email,
            "name": name,
            "password": password,
            "phone_no": phone_no,
            "gender": gender,
            "address": address
        }

        if request.method == 'POST':
            emailCheck = db['users'].find_one({'email' : email})
            print("Email cehck:", emailCheck)

            if(emailCheck):
                print("Email already exists")
                return redirect(url_for('register_page'))
            
            result = insert('users', data)
            
            if(result):
                print("Inserted Successfully")
                print(result)
                return redirect(url_for(f"home_page", user=user))
            else:
                print("Insertion Failed")
                print(result)

        return redirect(url_for(f"{role}_page", user=user))
    return render_template('register.html', register_form=register_form, user=user)

@app.route('/staff')
@logged_in
def staff_page():
    return render_template('staff.html', user=user)

@app.route('/reception')
@logged_in
def hospital_page():
    return render_template('reception.html', user=user)

@app.route('/doctor', methods=["GET", "POST"])
@logged_in
def doctor_page():
    stt_form = STTForm()
    text=None
    if stt_form.validate_on_submit():
        text = convert_speech_to_text('recorded/recorded-audio.wav')
    return render_template('doctor.html', user=user, stt_form=stt_form, text=text)

@app.route('/patient')
@logged_in
def patient_page():
    return render_template('patient.html', user=user)

@app.route('/pharmacy')
@logged_in
def pharmacy_page():
    return render_template('pharmacy.html', user=user)

@app.route('/camera')
def camera_page():
    return render_template('camera.html', user=user)

@app.route('/about-us')
def about_us_page():
    return render_template('about.html', user=user)

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
