from flask import Flask, request, render_template, send_file, jsonify
from digital_signature import DigitalSignature
import os

app = Flask(__name__)
ds = DigitalSignature()

# Tạo thư mục uploads nếu chưa tồn tại
if not os.path.exists('uploads'):
    os.makedirs('uploads')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_keys', methods=['POST'])
def generate_keys():
    ds.generate_key_pair()
    ds.save_keys()
    return jsonify({'message': 'Keys generated successfully'})

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    # Lưu file
    file_path = os.path.join('uploads', file.filename)
    file.save(file_path)

    # Ký số file
    signature_path = ds.sign_file(file_path)

    return jsonify({
        'message': 'File signed successfully',
        'file_path': file_path,
        'signature_path': signature_path
    })

@app.route('/verify', methods=['POST'])
def verify_file():
    if 'file' not in request.files or 'signature' not in request.files:
        return jsonify({'error': 'Missing file or signature'}), 400

    file = request.files['file']
    signature = request.files['signature']

    # Lưu file và chữ ký
    file_path = os.path.join('uploads', file.filename)
    signature_path = os.path.join('uploads', signature.filename)
    
    file.save(file_path)
    signature.save(signature_path)

    # Xác thực chữ ký
    is_valid = ds.verify_signature(file_path, signature_path)

    return jsonify({
        'is_valid': is_valid
    })

@app.route('/download/<filename>')
def download_file(filename):
    return send_file(os.path.join('uploads', filename))

if __name__ == '__main__':
    app.run(debug=True) 