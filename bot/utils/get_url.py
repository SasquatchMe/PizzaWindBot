def get_url(lon, lat):
    return (
        f"https://yandex.ru/maps/213/moscow/?ll={lat}%2C{lon}&"
        f"mode=whatshere&whatshere%5Bpoint%5D={lat}%2C{lon}&whatshere%5Bzoom%5D=15.45&z=14"
    )
