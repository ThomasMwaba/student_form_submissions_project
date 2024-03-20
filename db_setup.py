from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Student(Base):
    # Define table name
    __tablename__ = "students"
    # Define columns
    name = Column(String, index=True)  # Column for student name
    id = Column(Integer, primary_key=True, index=True)  # Primary key column
    grade5 = Column(Boolean, default=False)  # Column for grade 5, default to False
    grade6 = Column(Boolean, default=False)  # Column for grade 6, default to False
    grade7 = Column(Boolean, default=False)  # Column for grade 7, default to False
    project= Column(String, index=True)  # Column for project name
    progress = Column(String, index=True)  # Column for project progress
    hours = Column(Integer, index=True)  # Column for hours spent on the project
    subject = Column(String, index=True)  # Column for subject name
    active = Column(String, index=True)  # Column for study method
    method = Column(String, index = True)   # Column for how they did active recall

# Create an instance of the table
students_table = Student.__table__
