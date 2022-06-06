def sitio_entity(item) -> dict:
    return {
        'id': str(item['_id']),
        'nombre': item['nombre'],
        'descripcion': item['descripcion'],
        'latitud': item['latitud'],
        'longitud': item['longitud'],
        'tipo': item['tipo'],
        'sede': item['sede'],
        'estado': item['estado']
    }


def sitios_all(items) -> list:
    return [sitio_entity(item) for item in items]
