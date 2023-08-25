from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__, static_folder='static')
Bootstrap(app=app)
app.app_context().push()
app.secret_key = "secret-tunnel"

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/login')
def login_page():
    return render_template('login.html')

@app.route('/register')
def register_page():
    return render_template('register.html')

@app.route('/staff')
def staff_page():
    return render_template('staff.html')

@app.route('/reception')
def hospital_page():
    return render_template('reception.html')

@app.route('/doctor')
def doctor_page():
    return render_template('doctor.html')

@app.route('/patient')
def patient_page():
    return render_template('patient.html')

@app.route('/not_found')
@app.errorhandler(404)
def not_found(e):
    return render_template('not_found.html')

if __name__ == "__main__":
    app.run(debug=True)
