from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import models, schemas
from database import get_db

router = APIRouter()

@router.post("/menu/", response_model=schemas.MenuItemResponse)
def crear_menu_item(item: schemas.MenuItemCreate, db: Session = Depends(get_db)):
    nuevo_item = models.MenuItem(**item.dict())
    db.add(nuevo_item)
    db.commit()
    db.refresh(nuevo_item)
    return nuevo_item

@router.get("/menu/", response_model=list[schemas.MenuItemResponse])
def obtener_menu(db: Session = Depends(get_db)):
    return db.query(models.MenuItem).all()