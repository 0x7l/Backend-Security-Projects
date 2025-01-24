from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLAlchemy base
Base = declarative_base()

# Your existing User model
class User(Base):
    __tablename__ = "users"  # Ensure this matches your table name

    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
    mobile = Column(Integer)
    dob = Column(String)
    email = Column(String)
    name = Column(String)
    location = Column(String)
    fathername = Column(String)

# Update your database connection URL (MariaDB)
DATABASE_URL = "mysql+pymysql://root:llvll4@localhost/My_Project"  # Use your actual MariaDB credentials

# Create engine and session
engine = create_engine(DATABASE_URL, pool_size=10, max_overflow=20, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Ensure all tables are created (if they don't exist)
Base.metadata.create_all(bind=engine)
