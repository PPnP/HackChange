import pandas as pd
import requests
import json


class Geocoder(object):
    main_url = 'https://geocode-maps.yandex.ru/1.x/'
    params = {
        'geocoder': '',
        'apikey': 'ce89209d-a0f7-41ce-bde7-26d2aeab3269',
        'format': 'json'
    }

    def get_coords(self, data, f_out):
        coords = dict()
        for addr in data:
            Geocoder.params['geocode'] = addr
            r = requests.get(Geocoder.main_url, params=Geocoder.params)
            c = self.processing(r)
            if c is not None and 53.1 < float(c[0]) < 55.5 and 33 < float(c[1]) < 40:
                coords[addr] = c
        with open(f_out, 'w') as output:
            json.dump(coords, output)

    @staticmethod
    def processing(r):
        try:
            r.json()
        except json.decoder.JSONDecodeError:
            print('encoding error')
            return None
        else:
            r = r.json()
            if r['response']['GeoObjectCollection']['featureMember']:
                pos = r['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos']
                coords = list(reversed(pos.split()))
                return coords
            return None


gc = Geocoder()

# initial_data geocoder
# pd = pd.read_excel('data/initial_data.xlsx')
# addresses = list(pd['ADDRESS'])
# gc.get_coords(addresses, 'data/coords.json')

# post offices geocoder
f = open('data/post_offices.txt', 'r')
addresses = list([addr.strip() for addr in f])
f.close()
gc.get_coords(addresses, 'data/post_offices_coords.json')
