from typing import Union
from fastapi import FastAPI, Form

app = FastAPI()

app.post("/submit_form")
async def submit_form(firstname: str = Form(...),grade5: bool = Form(False),grade6: bool = Form(False),grade7: bool = Form(False),project_done: str = Form(...),project_hours: float = Form(...),subjectname: str = Form(...), subject_hours: float = Form(...), understanding: str = Form(...)):
    # accesses form fields like first name, grade , etc
    return {"message": "Form submitted successfully"}
    
     
