import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import hashes  # Correct import

def decrypt_folder(folder_path, private_key):
    with open('encrypted_aes_key.bin', 'rb') as key_file:
        encrypted_aes_key = key_file.read()

    # Debug: Print the loaded private key
    print("Loaded Private Key:", private_key)

    # Decrypt the AES key with the private key
    try:
        aes_key = private_key.decrypt(
            encrypted_aes_key,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
    except Exception as e:
        print("Decryption Error:", e)
        raise

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, 'rb') as f:
                encrypted_data = f.read()

            cipher = Cipher(algorithms.AES(aes_key), modes.CFB(b'\x00' * 16), default_backend())
            decryptor = cipher.decryptor()
            decrypted_data = decryptor.update(encrypted_data) + decryptor.finalize()

            with open(file_path, 'wb') as f:
                f.write(decrypted_data)


def main():
    # Define the path to the folder to be decrypted
    folder_to_decrypt = "/home/sec-lab/Dummy"

    # Load the unencrypted private key
    with open('private_key.pem', 'rb') as private_key_file:
        private_key = serialization.load_pem_private_key(
            private_key_file.read(),
            password=None,
            backend=default_backend()
        )

    # Decrypt each file in the folder
    decrypt_folder(folder_to_decrypt, private_key)

    print("Folder decrypted and unlocked successfully.")

if __name__ == "__main__":
    main()
