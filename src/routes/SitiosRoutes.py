# ------ FastAPI -------------
from fastapi import APIRouter, status
# ------ Libraries -----------
from config.MongoDB import db
from bson import ObjectId
# ------ Dependencies -------
from models.SitiosModel import Sitio
from schemas.SitioSchema import sitio_entity, sitios_all


sitio = APIRouter()


@sitio.get("/sitios",
           tags=["Sitios"],
           status_code=status.HTTP_200_OK,
           response_model=list[Sitio]
           )
async def get_all_sitios():
    all_sitios = db.Sitios.find()
    return sitios_all(all_sitios)


@sitio.get("/sitios/{id}",
           tags=["Sitios"],
           status_code=status.HTTP_200_OK,
           response_model=Sitio
           )
async def get_sitio(id: str):
    sitio = db.Sitios.find_one({'_id': ObjectId(id)})
    return sitio_entity(sitio)
