from pymongo import MongoClient
from decouple import config

url = config("MONGODB_URL")
coneccion = MongoClient(url)
db = coneccion.UbicateUC