import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.router import api_router

PROJECT_NAME = os.getenv("PROJECT_NAME", "Project APEX")
VERSION = os.getenv("VERSION", "0.1.0")
API_PREFIX = os.getenv("API_PREFIX", "/api/v1")

app = FastAPI(title=PROJECT_NAME, version=VERSION)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Link your clean, versioned router
app.include_router(api_router, prefix=API_PREFIX)

@app.get("/")
async def root_redirect():
    return {"message": f"Welcome to {PROJECT_NAME}. Access documentation at /docs"}
