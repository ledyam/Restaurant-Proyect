from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import models, schemas
from database import get_db

router = APIRouter(prefix='/menu')

@router.post("", response_model=schemas.MenuItemResponse , status_code=201 , )
def crear_menu_item(item: schemas.MenuItemCreate, db: Session = Depends(get_db)):
    nuevo_item = models.MenuItem(**item.model_dump())
    db.add(nuevo_item)
    db.commit()
    db.refresh(nuevo_item)
    raise HTTPException(status_code=201 , detail="Nuevo Platillo creado exitosamente")

@router.get("", response_model=list[schemas.MenuItemResponse])
def obtener_menu(db: Session = Depends(get_db)):
    
    current_menu : list[schemas.MenuItemResponse] = db.query(models.MenuItem).all()
     
    if not current_menu :
         
        raise HTTPException(status_code=204, detail="No se han encontrado platillos")
        
    else :  
        return current_menu
   