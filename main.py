from fastapi import FastAPI, HTTPException
from uuid import uuid4
from datetime import datetime, timedelta
from models import NoteIn, NoteOut
from utils import encrypt_note, decrypt_note
from database import save_note, get_note

app = FastAPI()

@app.post("/note", response_model=NoteOut)
def create_note(note: NoteIn):
    note_id = str(uuid4())
    encrypted = encrypt_note(note.content)
    expires_at = datetime.utcnow() + timedelta(seconds=note.ttl)
    save_note(note_id, encrypted, expires_at)
    
    note_url = f"http://localhost:8000/note/{note_id}"
    return {"note_url": note_url}

@app.get("/note/{note_id}")
def read_note(note_id: str):
    record = get_note(note_id)
    if not record:
        raise HTTPException(status_code=404, detail="Note not found or already viewed.")
    
    decrypted = decrypt_note(record["data"])
    return {"note": decrypted}
