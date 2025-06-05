from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.backends import default_backend
import base64
import os

class DigitalSignature:
    def __init__(self):
        self.private_key = None
        self.public_key = None

    def generate_key_pair(self):
        """Tạo cặp khóa RSA"""
        self.private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
            backend=default_backend()
        )
        self.public_key = self.private_key.public_key()

    def save_keys(self, private_key_path="private_key.pem", public_key_path="public_key.pem"):
        """Lưu cặp khóa vào file"""
        # Lưu private key
        with open(private_key_path, "wb") as f:
            f.write(self.private_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.PKCS8,
                encryption_algorithm=serialization.NoEncryption()
            ))

        # Lưu public key
        with open(public_key_path, "wb") as f:
            f.write(self.public_key.public_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo
            ))

    def load_keys(self, private_key_path="private_key.pem", public_key_path="public_key.pem"):
        """Đọc cặp khóa từ file"""
        # Đọc private key
        with open(private_key_path, "rb") as f:
            self.private_key = serialization.load_pem_private_key(
                f.read(),
                password=None,
                backend=default_backend()
            )

        # Đọc public key
        with open(public_key_path, "rb") as f:
            self.public_key = serialization.load_pem_public_key(
                f.read(),
                backend=default_backend()
            )

    def sign_file(self, file_path):
        """Ký số file"""
        with open(file_path, "rb") as f:
            file_data = f.read()

        # Tạo chữ ký
        signature = self.private_key.sign(
            file_data,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )

        # Lưu chữ ký vào file
        signature_path = file_path + ".sig"
        with open(signature_path, "wb") as f:
            f.write(signature)

        return signature_path

    def verify_signature(self, file_path, signature_path):
        """Xác thực chữ ký"""
        with open(file_path, "rb") as f:
            file_data = f.read()

        with open(signature_path, "rb") as f:
            signature = f.read()

        try:
            self.public_key.verify(
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