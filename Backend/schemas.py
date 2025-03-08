from pydantic import BaseModel, Field

class MenuItemBase(BaseModel):
    nombre: str
    descripcion: str
    precio: int
    categoria: str


class ReservaSchema(BaseModel):
    name: str
    identification: str 
    phone: str
    date: str
    time: str
    people: int
    message: str | None = None

class UsuariosSchema(BaseModel):
    
    name : str 
    identification : str 
    phone  : str 
    email  : str 
    ocupation : str  
    password : str 
 

class MenuItemCreate(MenuItemBase):
    pass

class MenuItemResponse(MenuItemBase):
    id: int

    class Config:
        orm_mode = True