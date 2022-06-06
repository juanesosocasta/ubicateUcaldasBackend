# ------ FastAPI -------------
from fastapi import APIRouter, status
# ------ Libraries -----------
from config.MongoDB import db
from bson import ObjectId
# ------ Dependencies -------
from models.SitiosModel import Sitio
from schemas.SitioSchema import sitio_entity, sitios_all

sitio = APIRouter()


@sitio.get("/sitios", tags=["Sitios"], 
           status_code=status.HTTP_200_OK,
           response_model=list[Sitio]
           )
async def get_all_sitios():
    return sitios_all(db.grafos.find())


@sitio.get("/sitios/{id}",
           tags=["Sitios"],
           status_code=status.HTTP_200_OK,
           response_model=Sitio
           )
async def get_sitio(id: str):
    grafo = db.grafos.find_one({'_id': ObjectId(id)})
    return sitio_entity(grafo)
