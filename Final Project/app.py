from flask import Flask, render_template, request, jsonify, send_from_directory
from werkzeug.utils import secure_filename
import os
import boto3

app = Flask(__name__)

# Configure upload folder and allowed extensions
UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# AWS Clients
translate_client = boto3.client('translate')
polly_client = boto3.client('polly')
rekognition_client = boto3.client('rekognition')

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    data = request.get_json()
    text = data['text']
    source_lang = data['source_lang']
    target_lang = data['target_lang']
    
    response = translate_client.translate_text(
        Text=text,
        SourceLanguageCode=source_lang,
        TargetLanguageCode=target_lang
    )
    translated_text = response['TranslatedText']
    return jsonify({"translated_text": translated_text})

@app.route('/speech', methods=['POST'])
def speech():
    data = request.get_json()
    text = data['text']
    
    # Generate speech with Polly
    response = polly_client.synthesize_speech(
        Text=text,
        OutputFormat='mp3',
        VoiceId='Joanna'
    )
    
    audio_filename = 'speech.mp3'
    audio_path = os.path.join(app.config['UPLOAD_FOLDER'], audio_filename)
    
    # Save audio file
    with open(audio_path, 'wb') as file:
        file.write(response['AudioStream'].read())
    
    return jsonify({"audio_url": f"/static/uploads/{audio_filename}"})

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['file']
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        
        # Analyze image with Rekognition
        with open(file_path, 'rb') as image:
            response = rekognition_client.detect_labels(
                Image={'Bytes': image.read()},
                MaxLabels=5
            )
        
        labels = [label['Name'] for label in response['Labels']]
        return jsonify({"image_url": f"/static/uploads/{filename}", "labels": labels})
    
    return jsonify({"error": "Invalid file type"}), 400

# Serve static files
@app.route('/static/uploads/<path:filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
