from fastapi import FastAPI, HTTPException, Depends, APIRouter
from pydantic import BaseModel
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database Setup (as you already have it)
DATABASE_URL = "mysql+pymysql://root:llvll4@localhost/My_Project"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# FastAPI instance
router = APIRouter()

# Pydantic model for login
class LoginRequest(BaseModel):
    username: str
    password: str

# Example database model (ensure this is defined as per your structure)
from sqlalchemy import Column, Integer, String

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(255), unique=True, index=True)
    password = Column(String(255))
    mobile = Column(Integer)
    dob = Column(String(255))
    email = Column(String(255))
    name = Column(String(255))
    location = Column(String(255))
    fathername = Column(String(255))

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/login")
async def login(request: LoginRequest, db: Session = Depends(get_db)):
    # Query the user from the database
    user = db.query(User).filter(User.username == request.username).first()
    
    if user is None or user.password != request.password:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    # Return the user data after login
    return {
        "message": "Login successful",
        "username": user.username,
        "mobile": user.mobile,
        "dob": user.dob,
        "email": user.email,
        "name": user.name,
        "location": user.location,
        "fathername": user.fathername,
    }
