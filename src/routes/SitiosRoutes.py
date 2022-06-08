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
    return sitios_all(db.Sitios.find())


@sitio.get("/sitios/{id}",
           tags=["Sitios"],
           status_code=status.HTTP_200_OK,
           response_model=Sitio
           )
async def get_sitio(id: str):
    grafo = db.Sitios.find_one({'_id': ObjectId(id)})
    return sitio_entity(grafo)

#create new site
@sitio.post("/sitios")
async def create_site(new_site : Sitio):
    response = db.Sitios.insert_one(dict(new_site)).inserted_id
    return sitio_entity(db.Sitios.find_one({'_id' : response}))