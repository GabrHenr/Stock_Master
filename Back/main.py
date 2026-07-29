from fastapi import FastAPI
from usuarios.routes import router as usuarios_routes

app = FastAPI()

app.include_router(usuarios_routes)