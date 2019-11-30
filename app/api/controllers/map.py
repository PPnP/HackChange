from flask.views import MethodView
from flask import render_template
from config import apikey
import json


class MapController(MethodView):
    def get(self):
        with open('DataAnalysis/data/coords.json', 'r', encoding='utf-8') as input:
            data = json.load(input)
        coords = list()
        i = 0
        for c in data.values():
            if i not in [407, 370, 214, 356, 357, 259, 390, 244, 293, 388, 324, 412, 261]:
                coords.append(c)
        return render_template('map.html', apikey=apikey, coords=coords)
