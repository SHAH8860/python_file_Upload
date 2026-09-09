from fastapi import FastAPI, UploadFile, File, Form
from database import SessionLocal, engine, Base
from schema import Student
import shutil
import os

app = FastAPI()

Base.metadata.create_all(bind=engine)

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@app.post("/students")
def create_student(
    name: str = Form(...),
    email: str = Form(...),
    file: UploadFile = File(...)
):
    db = SessionLocal()

    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    student = Student(
        name=name,
        email=email,
        file_path=file_path
    )

    db.add(student)
    db.commit()
    db.refresh(student)

    db.close()

    return {
        "id": student.id,
        "name": student.name,
        "email": student.email,
        "file": student.file_path
    }