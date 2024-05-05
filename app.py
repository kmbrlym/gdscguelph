import os
from flask import *
from model import generate

app = Flask(__name__)


def save_file(file, folder):
    if file:
        filename = file.filename
        file.save(os.path.join(app.static_folder, folder, filename))
        return filename

@app.route("/")
def index():
    return render_template("index.html")

# @app.route("/upload")
# def upload():
#     return render_template("upload.html")



@app.route("/upload", methods=['GET', 'POST'])
def upload_files():
    if request.method == "POST":
        # Check if the POST request has the file part
        if 'file1' in request.files and 'file2' in request.files:
            file1 = request.files['file1']
            file2 = request.files['file2']
            # Save the files to the upload folder
            file2.save(os.path.join('static', 'student-answer.pdf'))
            file1.save(os.path.join('static', 'marking-scheme.pdf'))
            # Redirect to a success page
            print("Files uploaded successfully")
            return redirect(url_for('feedback'))
    else :
        return render_template("upload.html")
      # Render upload page instead of redirecting

@app.route("/feedback")
def feedback():
    return render_template("feedback.html", response=generate())

    
if __name__ == "__main__":
    app.run(debug=True)
