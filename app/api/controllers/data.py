from flask.views import MethodView
import json


class DataController(MethodView):
    def get(self):
        with open('DataAnalysis/data/coords.json', 'r', encoding='utf-8') as input:
            data = json.load(input)
        coords = list()
        for c in data.values():
            coords.append(c)
        coords = json.dumps(coords)
        return coords
