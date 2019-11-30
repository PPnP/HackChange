import pandas as pd
import requests
import json


class Geocoder(object):
    data = pd.read_excel('data/initial_data.xlsx')
    addresses = list(data['ADDRESS'])
    main_url = 'https://geocode-maps.yandex.ru/1.x/'
    params = {
        'geocoder': '',
        'apikey': 'ce89209d-a0f7-41ce-bde7-26d2aeab3269',
        'format': 'json'
    }

    def get_coords(self):
        coords = dict()
        for addr in Geocoder.addresses:
            Geocoder.params['geocode'] = addr
            r = requests.get(Geocoder.main_url, params=Geocoder.params)
            coords[addr] = self.processing(r)
        with open('data/coords.json', 'w') as output:
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
            pos = r['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos']
            coords = list(reversed(pos.split()))
        return coords


gc = Geocoder()
gc.get_coords()
