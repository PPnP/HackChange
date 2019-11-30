from flask.views import MethodView
from flask import render_template
from config import apikey


class MapController(MethodView):
    def get(self):
        return render_template('map.html', apikey=apikey)
