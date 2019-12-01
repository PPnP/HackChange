import pandas as pd
import requests
import json
from math import isnan


class Geocoder(object):
    main_url = 'https://geocode-maps.yandex.ru/1.x/'
    params = {
        'geocoder': '',
        'apikey': 'ce89209d-a0f7-41ce-bde7-26d2aeab3269',
        'format': 'json'
    }

    def get_coords(self, data, f_out):
        coords = dict()
        for index, row in data.iterrows(): # for addr in data: | use it for coding post offices data
            Geocoder.params['geocode'] = row['ADDRESS']
            r = requests.get(Geocoder.main_url, params=Geocoder.params)
            c = self.processing(r)
            if c is not None and 53.1 < float(c[0]) < 55.5 and 33 < float(c[1]) < 40:
                postamat = 0                            # use 6 lines below only for coding initial data
                if not isnan(row['Postamat_daily']):
                    postamat = 1
                cashbox = 0
                if not isnan(row['cashbox_daily']):
                    cashbox = 1
                coords[row['ADDRESS']] = c + [str(postamat) + str(cashbox)]  # coords[row['ADDRESS']] = c | use it for coding post offices data
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
pd = pd.read_excel('data/initial_data.xlsx')
gc.get_coords(pd, 'data/coords.json')

# post offices geocoder
# f = open('data/post_offices.txt', 'r')
# addresses = list([addr.strip() for addr in f])
# f.close()
# gc.get_coords(addresses, 'data/post_offices_coords.json')
