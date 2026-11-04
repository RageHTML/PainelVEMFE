from dotenv_vault import load_dotenv
from sqlmodel import create_engine
import os

load_dotenv()
engine = create_engine(os.getenv("DATABASE_URL"), echo=True)