from pymongo import MongoClient
from decouple import config
#mongodb+srv://JoseManuel:*******@ubicateuc.c3jbt.mongodb.net/myFirstDatabase?retryWrites=true&w=majority

#url = config("mongodb+srv://JoseManuel:t4IUfatJA9XyyyvD@ubicateuc.c3jbt.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
coneccion = MongoClient("ConectionString")
db = coneccion.UbicateUC