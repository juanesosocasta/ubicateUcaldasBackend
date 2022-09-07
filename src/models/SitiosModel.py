from pydantic import BaseModel
from bson import ObjectId


class Sitio(BaseModel):
    _id: ObjectId
    nombre: str
    descripcion: str
    latitud: str
    longitud: str
    tipo: str
    sede: str
    estado: str
