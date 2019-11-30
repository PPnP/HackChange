from flask.views import MethodView
from flask import render_template
from config import apikey


class MapController(MethodView):
    def get(self):
        with open('DataAnalysis/data/coords.json', 'r', encoding='utf-8') as input:
            coords = input
        return render_template('map.html', apikey=apikey, coords=coords)
