from fastapi import FastAPI, Form
import asyncpg
from pydantic import BaseModel, Field

app = FastAPI()

# Define a function to create a database connection pool
async def get_pool():
    return await asyncpg.create_pool(
        user='my-database',
        password='Thomas4545',
        database='student_database',
        host='my-database.cniwyesmcch0.eu-west-2.rds.amazonaws.com',
        port=5432
    )

@app.post("/submit_form")
async def submit(first_name: str = Form(...),id: int = Form(...), grade5: bool = Form(False), grade6: bool = Form(False), grade7: bool = Form(False), project_name: str = Form(...), project_progress: str = Form(...), project_hours: float = Form(...), subject_name: str = Form(...), study_method: str = Form(...)):
    # Access form fields like first name, grade, etc.
    async with get_pool() as pool:
        async with pool.acquire() as conn:
            # Define the SQL query to insert form data into the database table
            query = "INSERT INTO students (first_name,id, grade5, grade6, grade7, project_name, project_progress, project_hours, subject_name, study_method) VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9, $10)"
            # Execute the SQL query with form data as parameters
            row = await conn.fetchrow(query, id, first_name, grade5, grade6, grade7, project_name, project_progress, project_hours, subject_name, study_method, subject_hours)
            return row
