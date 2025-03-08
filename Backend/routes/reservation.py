from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import models, schemas
from database import get_db


router = APIRouter()


@router.post("/reserva", response_model=schemas.ReservaSchema)
def crear_reserva(reserva: schemas.ReservaSchema, db: Session = Depends(get_db)):
    nueva_reserva = models.Reserva(**reserva.dict())
    db.add(nueva_reserva)
    db.commit()
    db.refresh(nueva_reserva)

    return {
        "name": nueva_reserva.name,
        "identification": nueva_reserva.identification,
        "phone": nueva_reserva.phone,
        "date": str(nueva_reserva.date),  # Convertir a string
        "time": str(nueva_reserva.time),  # Convertir a string
        "people": nueva_reserva.people,
        "message": nueva_reserva.message,
    }