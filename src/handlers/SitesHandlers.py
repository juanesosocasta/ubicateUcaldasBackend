from config.MongoDB import db
from bson import ObjectId


def get_all_sites(tipo, nombre):
    items_inquiry = {}

    if tipo:
        items_inquiry['tipo'] = tipo

    if nombre:
        items_inquiry['nombre'] = {'$regex': nombre}

    all_sitios = db.Sitios.find(items_inquiry)
    return all_sitios


def get_site(id):
    sitio = db.Sitios.find_one({'_id': ObjectId(id)})
    return sitio


def get_filter_sites_by_name(name):
    all_sitios = db.Sitios.find({"nombre": {'$regex': name}})
    return list(all_sitios)
