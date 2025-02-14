from pydantic import BaseModel

class MenuItemBase(BaseModel):
    nombre: str
    descripcion: str
    precio: int
    categoria: str

class MenuItemCreate(MenuItemBase):
    pass

class MenuItemResponse(MenuItemBase):
    id: int

    class Config:
        orm_mode = True