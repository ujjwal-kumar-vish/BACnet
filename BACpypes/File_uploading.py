from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/upload')
def upload_form():
    return render_template('upload.html')

@app.route('/uploader', methods=['POST'])
def handle_upload():
    if 'file' not in request.files:
        return 'No file part in the request'
    
    f = request.files['file']
    if f.filename == '':
        return 'No selected file'
    
    filename = secure_filename(f.filename)
    f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return 'File uploaded successfully'

if __name__ == '__main__':
    app.run(debug=True)