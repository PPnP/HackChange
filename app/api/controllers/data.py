from flask.views import MethodView
import json


class DataController(MethodView):
    def get(self):
        with open('DataAnalysis/data/coords.json', 'r', encoding='utf-8') as input:
            data = json.load(input)
        coords = list()
        i = 0
        for c in data.values():
            if i not in [407, 370, 214, 356, 357, 259, 390, 244, 293, 388, 324, 412, 261]:
                coords.append(c)
        coords = json.dumps(coords)
        return coords
