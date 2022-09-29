from pymongo import MongoClient
from decouple import config

from dotenv import load_dotenv

load_dotenv()

url = config("MONGODB_URL")
coneccion = MongoClient(url)
db = coneccion.UbicateUC
