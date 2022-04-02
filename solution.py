def select_params(json_response):
    toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
    toponym_coodrinates = toponym["Point"]["pos"]
    toponym_longitude, toponym_lattitude = toponym_coodrinates.split(" ")
    delta = str(int(input('Размеры объекта: ')) / 100)
    x, y = toponym_longitude, toponym_lattitude
    point = "{0},{1}".format(x, y)
    map_params = {
        "ll": ",".join([toponym_longitude, toponym_lattitude]),
        "spn": ",".join([delta, delta]),
        "l": "map",
        'pt': "{0},pm2dgl".format(point)
    }
    return map_params