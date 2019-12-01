from flask.views import MethodView
import json


class DataController(MethodView):
    def get(self):
        with open('DataAnalysis/data/toMap.json', 'r', encoding='utf-8') as data:
            coords = json.load(data)
        coords = json.dumps(coords)
        return coords
