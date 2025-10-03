from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker, declarative_base
from werkzeug.security import generate_password_hash, check_password_hash

# Create a class database
Base = declarative_base()

# Class user
class User(Base):

    #Which table use for class
    __tablename__ = 'users'

    #Features 
    id = Column(Integer, primary_key=True)
    username = Column(String(30), unique=True, nullable=False)
    email = Column(String(254), unique=True, nullable=False)
    password_hash = Column(String(128))

    #Functions for generate password hash and check it
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    # Function to report about user
    def __repr__(self):
        return f"<User(id={self.id}, name='{self.name}', email='{self.email}')>"
# Create database
engine = create_engine(r"sqlite:///C:\Users\Павел\Documents\GitHub\Mini\app\database.db")
Base.metadata.create_all(engine)