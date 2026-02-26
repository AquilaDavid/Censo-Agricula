import os
import logging
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DATABASE_DIR = os.path.join(BASE_DIR, "database")

os.makedirs(DATABASE_DIR, exist_ok=True)

class Config:
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(DATABASE_DIR, 'censo.db')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    LOG_LEVEL = logging.INFO