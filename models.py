from pydantic import BaseModel

class NoteIn(BaseModel):
    content: str
    ttl: int  # Time to live in seconds

class NoteOut(BaseModel):
    note_url: str

