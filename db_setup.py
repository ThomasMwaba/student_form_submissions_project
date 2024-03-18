from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Student(Base):
    # Define table name
    __tablename__ = "students"
    # Define columns
    id = Column(Integer, primary_key=True, index=True)  # Primary key column
    name = Column(String, index=True)  # Column for student name
    school_id = Column(Integer, index=True)  # Column for student school ID
    grade5 = Column(Boolean, default=False)  # Column for grade 5, default to False
    grade6 = Column(Boolean, default=False)  # Column for grade 6, default to False
    grade7 = Column(Boolean, default=False)  # Column for grade 7, default to False
    project_name = Column(String, index=True)  # Column for project name
    project_progress = Column(String, index=True)  # Column for project progress
    project_hours = Column(Integer, index=True)  # Column for hours spent on the project
    subject_name = Column(String, index=True)  # Column for subject name
    study_method = Column(String, index=True)  # Column for study method

# Create an instance of the table
students_table = Student.__table__
