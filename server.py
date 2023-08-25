from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__, static_folder='static')
Bootstrap(app=app)
app.app_context().push()
app.secret_key = "secret-tunnel"

@app.route('/')
def home_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
