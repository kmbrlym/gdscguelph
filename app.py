from flask import Flask, render_template, request
import os

app = Flask(__name__)

app_data = {'project_name': 'name'}
app.secret_key = 'your_secret_key_here'

@app.route("/")
def index():
    return render_template("index.html", app_data=app_data)

@app.route("/upload", methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        try:
            # Get the uploaded files
            marking_scheme_file = request.files['file1']
            student_answer_file = request.files['file2']

            # Save the uploaded files as PDFs
            marking_scheme_file.save(os.path.join('static', 'markingscheme.pdf'))
            student_answer_file.save(os.path.join('static', 'studentanswer.pdf'))

            # Redirect or render a success page
            return 'Files uploaded successfully!'
        except Exception as e:
            return f'An error occurred: {str(e)}'
    else:
        return render_template('upload.html', app_data=app_data)
    
if __name__ == "__main__":
    app.run(debug=True)
