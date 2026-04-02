import os
from dotenv import load_dotenv

#carga las variables de entorno
load_dotenv()

class Settings:
    PROJECT_NAME= STR = "ZEN SAVE API"
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./zensave.db")
    SECRET_KEY: str = os.getenv("SECRET-KEY", "368f89885e925503327211fe08448fd0aeb511850d22cb1e71df095b3b48d2f")
    ALGORITHM: str = os.getenv("ALGORITHM", "HS256")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30))

    GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY", "nodefinida")

#habilitar la configuracion para utilizarla en toda la app
settings = Settings()
