from fastapi import FastAPI
from routes import router as main_route

app = FastAPI()

app.include_router(main_route)