import re
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, SelectField, IntegerField, TextAreaField, RadioField, validators
from wtforms.validators import DataRequired

def validate_phone_number(form, field):
    phone_number_pattern = r'^\d{10}$' 

    if not re.match(phone_number_pattern, field.data):
        raise validators.ValidationError('Invalid phone number format')
class DiseaseDetailsForm(FlaskForm):
    pass

class PatientDetailsForm(FlaskForm):
    pass

class LoginUserForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    role = SelectField("Role", choices=[("doctor", "Doctor"), ("reception", "Reception"), ("staff", "Staff"), ("patient", "Patient"), ("pharmacy", "Pharmacy")])
    submit = SubmitField("Log In")

class RegisterUserForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    role = SelectField("Role", choices=[("doctor", "Doctor"), ("reception", "Reception"), ("staff", "Staff"), ("patient", "Patient"), ("pharmacy", "Pharmacy")])
    phone_no = StringField("Phone No.", validators=[DataRequired(), validate_phone_number])
    gender = SelectField("Gender", validators=[DataRequired()], choices=[("male", "Male"), ("female", "Female"), ("other", "Other")])
    address = TextAreaField("Address", validators=[DataRequired()])
    submit = SubmitField("Register")
