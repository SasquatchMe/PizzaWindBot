from geopy.distance import geodesic


def check_geopos(coord_user, coord_req):
    dist = geodesic(coord_user, coord_req).kilometers

    return True  # dist < 0.5
