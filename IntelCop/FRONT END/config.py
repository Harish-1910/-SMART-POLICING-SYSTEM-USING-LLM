import os

class Config:
    SECRET_KEY = 'a8f9c3e2b7d4f1e6c5a2d9b0e7f4c6a3'  # Use a strong key like this
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

