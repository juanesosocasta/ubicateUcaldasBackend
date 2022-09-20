from pymongo import MongoClient
from decouple import config

#url = config("MONGODB_URL")
coneccion = MongoClient(
    "mongodb+srv://ubicateuc:KqCV9CYcZAbR46YZ@ubicateuc.c3jbt.mongodb.net/test")
db = coneccion.UbicateUC
