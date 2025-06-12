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
    return render_template('sender.html')

@app.route('/sender')
def sender():
    return render_template('sender.html')

@app.route('/receiver')
def receiver():
    return render_template('receiver.html')

@app.route('/generate_keys', methods=['POST'])
def generate_keys():
    username = request.json.get('username')
    if not username:
        return jsonify({'error': 'Missing username'}), 400
    
    private_key_path = f"{username}_private_key.pem"
    public_key_path = f"{username}_public_key.pem"

    ds.generate_key_pair()
    ds.save_keys(private_key_path=private_key_path, public_key_path=public_key_path)
    return jsonify({'message': f'Keys generated successfully for {username}'})

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
        'file_path': file.filename,
        'signature_path': os.path.basename(signature_path)
    })

@app.route('/get_public_key/<username>', methods=['GET'])
def get_public_key(username):
    public_key_path = f"{username}_public_key.pem"
    if not os.path.exists(public_key_path):
        return jsonify({'error': 'Public key not found for this username'}), 404
    return send_file(public_key_path)

@app.route('/verify', methods=['POST'])
def verify_file():
    # Expect filenames as form data, not file uploads
    file_name = request.form.get('file_name')
    signature_name = request.form.get('signature_name')
    username = request.form.get('username')

    if not file_name or not signature_name or not username:
        return jsonify({'error': 'Missing file name, signature name, or username'}), 400

    # Construct full paths on the server
    file_path = os.path.join('uploads', file_name)
    signature_path = os.path.join('uploads', signature_name)

    # Check if files exist on the server
    if not os.path.exists(file_path):
        return jsonify({'error': f'File \'{file_name}\' not found on server.'}), 404
    if not os.path.exists(signature_path):
        return jsonify({'error': f'Signature file \'{signature_name}\' not found on server.'}), 404

    # Tải khóa công khai của người gửi
    public_key_path = f"{username}_public_key.pem"
    if not os.path.exists(public_key_path):
        return jsonify({'error': 'Public key not found for this username.'}), 404
    
    ds.load_keys(public_key_path=public_key_path)

    # Xác thực chữ ký
    is_valid = ds.verify_signature(file_path, signature_path)

    return jsonify({
        'is_valid': is_valid
    })

@app.route('/download/<filename>')
def download_file(filename):
    return send_file(os.path.join('uploads', filename))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0') 