from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
import models
from database import get_db

router = APIRouter()

@router.get("/user-exists/{username}/{password}")
async def check_user(username: str, password: str, db: AsyncSession = Depends(get_db)):
    # Creamos la consulta
    stmt = select(models.Usuarios).filter(models.Usuarios.username == username, models.Usuarios.password == password)
    
    # Ejecutamos la consulta de manera asíncrona
    result =  db.execute(stmt)
    
    # Obtenemos el primer usuario usando scalars() para obtener solo la columna que nos interesa
    user = result.scalars().first()
    
    if user:
        return {"message": "El usuario existe", "exists": True}
    else:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
