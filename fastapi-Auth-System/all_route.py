from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime
from model import User, SessionLocal

router = APIRouter()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Signup route to save data to the existing database
@router.post("/signup")
async def signup(
    username: str, 
    password: str, 
    mobile: int, 
    dob: str, 
    email: str,
    name: str, 
    location: str, 
    fathername: str,
    db: Session = Depends(get_db)  # Get the database session
):
    # Convert dob string to date object
    try:
        dob_date = datetime.strptime(dob, "%Y-%m-%d").date()  # Convert dob to datetime object
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid date format. Use YYYY-MM-DD")

    # Create new user instance
    new_user = User(
        username=username,
        password=password,
        mobile=mobile,
        dob=dob_date,
        email=email,
        name=name,
        location=location,
        fathername=fathername
    )

    # Add the new user to the database
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        "message": "Signup successful", 
        "username": new_user.username, 
        "password": new_user.password, 
        "name": new_user.name, 
        "mobile": new_user.mobile, 
        "dob": new_user.dob, 
        "email": new_user.email, 
        "location": new_user.location, 
        "fathername": new_user.fathername
    }
