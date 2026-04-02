from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.core.config import settings

#engine va a ser el motor encargado de la conexion
engine = create_engine(
    settings.DATABASE_URL, connect_args={"check_same_thread": False}

)

#para crear sesiones locales 
SessionLocal = sessionmaker(autocomit=False, autoflush=False, bind=engine)

#Base para nuestros modelos de tablas
Base = declarative_base()

#dependencia de FastAPI

def get_db():
    db = SessionLocal()

    try:
        yield db
    finally: 
        db.close()