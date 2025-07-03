from pymongo import MongoClient
from datetime import datetime, timedelta
import os

MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27017")
client = MongoClient(MONGO_URL)
db = client.snapnote

def save_note(note_id: str, encrypted_note: str, expires_at: datetime):
    db.notes.insert_one({
        "_id": note_id,
        "data": encrypted_note,
        "expires_at": expires_at
    })

def get_note(note_id: str):
    return db.notes.find_one_and_delete({"_id": note_id})
