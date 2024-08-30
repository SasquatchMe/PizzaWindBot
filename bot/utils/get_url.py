def get_url(lon, lat):
    return (f'https://yandex.ru/maps/213/moscow/?ll={lon}%2C{lat}&'
            f'mode=whatshere&whatshere%5Bpoint%5D={lon}%2C{lat}&whatshere%5Bzoom%5D=15.45&z=14')