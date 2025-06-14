from flask import Flask, render_template, request, redirect, url_for, flash, send_from_directory
from werkzeug.utils import secure_filename
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'docx'}

# Tạo thư mục nếu chưa tồn tại
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

def sign_file(private_key_path, file_path):
    with open(private_key_path, "rb") as key_file:
        private_key = serialization.load_pem_private_key(
            key_file.read(),
            password=None,
            backend=default_backend()
        )
    
    with open(file_path, "rb") as f:
        data = f.read()
    
    signature = private_key.sign(
        data,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    
    return signature

def verify_signature(public_key_path, file_data, signature):
    with open(public_key_path, "rb") as key_file:
        public_key = serialization.load_pem_public_key(
            key_file.read(),
            backend=default_backend()
        )
    
    try:
        public_key.verify(
            signature,
            file_data,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return True
    except Exception:
        return False

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # Kiểm tra file
        if 'file' not in request.files:
            flash('Không có file được chọn')
            return redirect(request.url)
        
        file = request.files['file']
        if file.filename == '':
            flash('Không có file được chọn')
            return redirect(request.url)
        
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            
            # Ký số file
            try:
                signature = sign_file('private_key.pem', filepath)
                signature_filename = filename + '.sig'
                signature_path = os.path.join(app.config['UPLOAD_FOLDER'], signature_filename)
                
                with open(signature_path, 'wb') as f:
                    f.write(signature)
                
                flash('File đã được upload và ký số thành công!')
                return render_template('upload.html', 
                                    filename=filename,
                                    signature_filename=signature_filename)
            
            except Exception as e:
                flash(f'Lỗi khi ký số: {str(e)}')
                return redirect(request.url)
    
    return render_template('upload.html')

@app.route('/download', methods=['GET', 'POST'])
def download():
    if request.method == 'POST':
        file = request.files['file']
        signature_file = request.files['signature']
        
        if file and signature_file:
            file_data = file.read()
            signature = signature_file.read()
            
            # Xác thực chữ ký
            is_valid = verify_signature('public_key.pem', file_data, signature)
            
            if is_valid:
                flash('Chữ ký hợp lệ! File đã được xác thực.')
            else:
                flash('Cảnh báo: Chữ ký không hợp lệ! File có thể đã bị thay đổi.')
            
            return render_template('download.html', 
                                validation_result=is_valid,
                                filename=file.filename)
    
    return render_template('download.html')

@app.route('/download_file/<filename>')
def download_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True,port=5000)
    