import os
from dotenv import load_dotenv
from cryptography.fernet import Fernet

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
if not SECRET_KEY:
    raise ValueError("SECRET_KEY is missing in .env")

cipher = Fernet(SECRET_KEY.encode())

def encrypt_note(plain_text: str) -> str:
    return cipher.encrypt(plain_text.encode()).decode()

def decrypt_note(encrypted_text: str) -> str:
    return cipher.decrypt(encrypted_text.encode()).decode()
