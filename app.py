from flask import *

app = Flask(__name__)

app_data = {'project_name': 'name'}
app.secret_key = 'your_secret_key_here'

@app.route("/")
def index():
    return render_template("index.html", app_data=app_data)

@app.route("/upload.html")
def upload():
    return render_template("upload.html", app_data=app_data)

if __name__ == "__main__":
    app.run(debug=True)
