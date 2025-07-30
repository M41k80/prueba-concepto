from sqlmodel import SQLModel, create_engine, Session
import os
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
engine = create_engine(SUPABASE_URL, echo=True)

def init_db():
    SQLModel.metadata.create_all(engine)

# Crear sesión para cada request FastAPI
def get_db():
    with Session(engine) as session:
        yield session
