# main.py

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import os

from .database import Base, engine
from .api.routes import router

app = FastAPI(title="AI Image Studio")

# CORS
cors_origins = os.getenv("CORS_ORIGINS", "*")
if cors_origins == "*":
    allow_origins = ["*"]
else:
    allow_origins = [origin.strip() for origin in cors_origins.split(",") if origin.strip()]

app.add_middleware(
    CORSMiddleware,
    allow_origins=allow_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# create tables
Base.metadata.create_all(bind=engine)

# include routes
app.include_router(router)


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/")
def root():
    return {"message": "AI Image Studio API is running"}


# absolute path to images folder
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
images_path = os.path.join(BASE_DIR, "images")

# serve images
app.mount("/images", StaticFiles(directory=images_path), name="images")