from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, SelectField, IntegerField, TextAreaField, RadioField
from wtforms.validators import DataRequired
from Disease import list_column_names

column_names = list_column_names("dataset/Training.csv")
class DiseaseDetailsForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    disease_list = SelectField("Disease", choices=[(column_name, column_name) for column_name in column_names])
    submit = SubmitField("Submit")

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

# class AddMedicineForm(FlaskForm):
#     name = StringField("Name", validators=[DataRequired()])
#     description = TextAreaField("Description", validators=[DataRequired()])
#     price = IntegerField("Price", validators=[DataRequired()])
#     quantity = IntegerField("Quantity", validators=[DataRequired()])
#     submit = SubmitField("Add")

class STTForm(FlaskForm):
    submit = SubmitField("Submit")