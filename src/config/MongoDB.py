from pymongo import MongoClient
from decouple import config
url = config("MONGOURL")
coneccion = MongoClient(url)
db = coneccion.UbicateUC