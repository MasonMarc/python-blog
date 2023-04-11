from app.db import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import validates
import bcrypt

salt = bcrypt.gensalt()

class User(Base):
  __tablename__ = 'users'
  id = Column(Integer, primary_key=True)
  username = Column(String(50), nullable=False)
  email = Column(String(50), nullable=False, unique=True)
  password = Column(String(100), nullable=False)

  def verify_password(self, password):
    return bcrypt.checkpw(
      password.encode('utf-8'),
      self.password.encode('utf-8')
    )
  
  @validates('email')
  def validate_email(self, key, email):
    assert '@' in email 
    # ensures @ is present in string

    return email
  
  @validates('password')
  def validate_password(self, key, password):
    assert len(password) > 4
    # ensures password is at least 5 chars


    return bcrypt.hashpw(password.encode('utf-8'), salt)