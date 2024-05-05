from flask import *
import os 

app = Flask(__name__)

app_data = {'project_name': 'name'}
app.secret_key = 'your_secret_key_here'

def save_file(file, folder):
    if file:
        filename = file.filename
        file.save(os.path.join(app.static_folder, folder, filename))
        return filename

@app.route("/")
def index():
    return render_template("index.html", app_data=app_data)

@app.route("/upload", methods=['GET', 'POST'])
def upload_files():
    if request.method == "POST":
        # Check if the POST request has the file part
        if 'file1' in request.files and 'file2' in request.files:
            file1 = request.files['file1']
            file2 = request.files['file2']
            # Save the files to the upload folder
            file1.save(os.path.join('static', file1.filename))
            file2.save(os.path.join('static', file2.filename))
            # Redirect to a success page
            print("Files uploaded successfully")
            return redirect(url_for('upload_success'))
    print("Reached GET method or file upload failed, redirecting to upload page")
    return render_template("upload.html", app_data=app_data)  # Render upload page instead of redirecting



@app.route("/upload_success")
def upload_success():
    return "Files uploaded successfully!"


if __name__ == "__main__":
    app.run(debug=True)
