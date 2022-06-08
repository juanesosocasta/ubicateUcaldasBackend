from turtle import st
from typing import Optional
from pydantic import BaseModel
from bson import ObjectId


class Sitio(BaseModel):

    #_id: ObjectId
    nombre: str
    descripcion: str
    latitud: float
    longitud: float
    tipo: str
    sede: str
    estado: bool
