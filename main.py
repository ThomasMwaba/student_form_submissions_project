from fastapi import FastAPI, Form
import asyncpg
from pydantic import BaseModel, Field

app = FastAPI()

# Define a function to create a database connection pool
async def get_pool():
    return await asyncpg.create_pool(
        user='postgres',
        password='Thomas4545',
        database='my-database',
        host='my-database.cniwyesmcch0.eu-west-2.rds.amazonaws.com',
        port=5432
    )

@app.post("/submit_form")
async def submit(name: str = Form(...),id: int = Form(...), grade5: bool = Form(False), grade6: bool = Form(False), grade7: bool = Form(False), project: str = Form(...), progress: str = Form(...), hours: int = Form(...), subject: str = Form(...), active: str = Form(...),method: str = Form(...)):
    # Access form fields like first name, grade, etc.
    pool = await get_pool()
    async with pool.acquire() as conn:
        # Define the SQL query to insert form data into the database table
        query = "INSERT INTO students (name,id, grade5, grade6, grade7, project, progress, hours, subject, method) VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9, $10,$11)"
        # Execute the SQL query with form data as parameters
        row = await conn.fetchrow(query,name,id, grade5, grade6, grade7, project, progress, hours, subject, active, method)
        return row
