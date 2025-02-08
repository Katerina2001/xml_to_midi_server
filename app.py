from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import os
from music21 import converter

app = Flask(__name__)
CORS(app)  # Allow communication from Flutter

# Folder settings
UPLOAD_FOLDER = 'uploads'
OUTPUT_FOLDER = 'outputs'
AUDIVERIS_DIR = 'C:/Users/alexi/audiveris/build'  # Audiveris folder

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

def run_audiveris(image_path, output_dir):
    try:
        libs_path = os.path.join(AUDIVERIS_DIR, 'libs', '*')  # All JAR files in the libs folder
        command = f'java -cp "{libs_path};{AUDIVERIS_DIR}/jar/Audiveris.jar" org.audiveris.omr.Main -batch {image_path} -output {output_dir} -export'
        os.system(command)
        return True
    except Exception as e:
        return str(e)

def convert_musicxml_to_midi(xml_path, midi_path):
    try:
        score = converter.parse(xml_path)
        score.write('midi', fp=midi_path)
        return True
    except Exception as e:
        return str(e)

def get_musicxml_key(xml_path):
    try:
        score = converter.parse(xml_path)
        key_signature = score.analyze('key')
        tonic = key_signature.tonic.name  # Key tonic (e.g., C, D, E♭)
        mode = key_signature.mode         # Major or Minor
        return {'tonic': tonic, 'mode': mode, 'key': f'{tonic} {mode}'}
    except Exception as e:
        return {'error': str(e)}

@app.route('/process', methods=['POST'])
def process_image():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)

    output_dir = os.path.join(OUTPUT_FOLDER, os.path.splitext(file.filename)[0])
    os.makedirs(output_dir, exist_ok=True)

    # Run Audiveris
    result = run_audiveris(file_path, output_dir)
    if result is not True:
        return jsonify({'error': f'Audiveris error: {result}'}), 500

    # Convert to MIDI
    xml_file = os.path.join(output_dir, os.path.splitext(file.filename)[0] + '.mxl')
    midi_file = os.path.join(output_dir, 'output.mid')
    midi_result = convert_musicxml_to_midi(xml_file, midi_file)
    if midi_result is not True:
        return jsonify({'error': f'MIDI conversion error: {midi_result}'}), 500

    # Get Key Signature
    key_signature = get_musicxml_key(xml_file)

    return jsonify({
        'midi_url': f'/download/midi/{os.path.basename(midi_file)}',
        'xml_url': f'/download/xml/{os.path.basename(xml_file)}',
        'key_signature': key_signature
    })

@app.route('/download/<file_type>/<filename>', methods=['GET'])
def download_file(file_type, filename):
    folder = OUTPUT_FOLDER if file_type in ['xml', 'midi'] else OUTPUT_FOLDER
    file_path = os.path.join(folder, filename)
    if os.path.exists(file_path):
        return send_file(file_path, as_attachment=True)
    return jsonify({'error': 'File not found'}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
