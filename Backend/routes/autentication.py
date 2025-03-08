from fastapi.security import OAuth2PasswordBearer , OAuth2PasswordRequestForm
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from Backend import models
from Backend.schemas import UsuariosSchema
from database import get_db
from sqlalchemy.orm import Session

router = APIRouter(prefix='/autentication')
oauth2 = OAuth2PasswordBearer(tokenUrl="login")
router = APIRouter()
@router.post("/login")
async def login(form :OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)) :
    stmt = select(models.Usuarios).filter(models.Usuarios.username == form.username, models.Usuarios.password == form.password)
    
    result =  db.execute(stmt)
    user = result.scalars().first()

    if user.username != form.username:
        raise HTTPException(status_code=400 ,detail="Usuario no encontrado")
    
    if user.password != form.password : 
        raise HTTPException(status_code=400 ,detail="Contraseña Incorrecta")    

    return {"access_token" : user.name, "token_type" : "bearer" }

@router.get("users/me")
async def me (user : UsuariosSchema = Depends(current_user)): 
    return user 

async def current_user (token : str Depends(oauth2)):
    pass