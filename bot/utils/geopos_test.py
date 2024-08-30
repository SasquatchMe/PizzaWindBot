from geopy.distance import geodesic, distance


def check_geopos(coord_user, coord_req):
    dist = geodesic(coord_user, coord_req).kilometers

    return dist < 0.05
