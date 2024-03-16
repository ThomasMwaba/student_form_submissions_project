from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import databases

# PostgreSQL connection URL
DATABASE_URL = "postgresql://my-database:Thomas4545@my-database.cniwyesmcch0.eu-west-2.rds.amazonaws.com:5432/student_database"

# Create a databases database instance for asynchronous support
database = databases.Database(DATABASE_URL)

# SQLAlchemy engine for synchronous operations
engine = create_engine(DATABASE_URL)

# Create a sessionmaker for database interactions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Define base class for SQLAlchemy models
Base = declarative_base()


# Define Database Models

# This class represents the "students" table in the database
class Students(Base):
    # Define table name
    __tablename__ = "students"
    # Define columns
    name = Column(String, index=True)  # Column for student name
    id = Column(Integer, primary_key=True, index=True)  # Primary key column
    grade = Column(String, index=True)  # Column for student grade
    project_name = Column(String, index=True)  # Column for project name
    progress = Column(String, index=True)  # Column for project progress
    hours_spent = Column(Float, index=True)  # Column for hours spent on the project
    subject_name = Column(String, index=True)  # Column for subject name
    method = Column(String, index=True)  # Column for study method
    hours_spent = Column(Float, index=True)  # Column for hours spent studying