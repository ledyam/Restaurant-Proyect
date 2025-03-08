from fastapi import FastAPI
import models
from database import engine
from routes import menu , reservation , users
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Cambia "*" por ["http://localhost:3000"] si usas React o el puerto correcto de tu frontend
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos los métodos (GET, POST, etc.)
    allow_headers=["*"],  # Permite todos los headers
)
models.Base.metadata.create_all(bind=engine)

app.include_router(menu.router)
app.include_router(reservation.router)
app.include_router(users.router)