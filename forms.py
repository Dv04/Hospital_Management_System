from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, SelectField, IntegerField, TextAreaField, RadioField
from wtforms.validators import DataRequired

class DiseaseDetailsForm(FlaskForm):
    pass

class PatientDetailsForm(FlaskForm):
    pass

class LoginUserForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    role = SelectField("Role", choices=[("doctor", "Doctor"), ("reception", "Reception"), ("staff", "Staff"), ("patient", "Patient"), ("pharmacy", "Pharmacy")])
    submit = SubmitField("Sign In")

class RegisterUserForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    role = SelectField("Role", choices=[("doctor", "Doctor"), ("reception", "Reception"), ("staff", "Staff"), ("patient", "Patient"), ("pharmacy", "Pharmacy")])
    phone_no = IntegerField("Phone No.", validators=[DataRequired()])
    gender = SelectField("Gender", validators=[DataRequired()], choices=[("male", "Male"), ("female", "Female"), ("other", "Other")])
    address = TextAreaField("Address", validators=[DataRequired()])
    submit = SubmitField("Register")
