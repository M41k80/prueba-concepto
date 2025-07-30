from fastapi import FastAPI, APIRouter, Depends
from sqlalchemy.orm import Session
import db
import models
import schemas
import auth
from auth import get_current_user
from models import User
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()




app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def on_startup():
    db.init_db()

@app.get("/")
def root():
    return {"message": "API is running 🚀"}

@app.post("/register")
def register(user: schemas.UserCreate, session: Session = Depends(db.get_db)):
    return auth.register(user, session)

@app.post("/login", response_model=schemas.TokenResponse)
def login(user: schemas.UserLogin, session: Session = Depends(db.get_db)):
    return auth.login(user, session)

router = APIRouter()

@router.get("/me")
def read_current_user(current_user: User = Depends(get_current_user)):
    return {
        "email": current_user.email,
        "id": current_user.id,
    }

app.include_router(router)
