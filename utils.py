from cryptography.fernet import Fernet

# Generate a key once and store securely (env var or config)
SECRET_KEY = Fernet.generate_key()
cipher = Fernet(SECRET_KEY)

def encrypt_note(plain_text: str) -> str:
    return cipher.encrypt(plain_text.encode()).decode()

def decrypt_note(encrypted_text: str) -> str:
    return cipher.decrypt(encrypted_text.encode()).decode()
