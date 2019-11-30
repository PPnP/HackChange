from flask.views import MethodView
from flask import render_template


class MapController(MethodView):
    def get(self):
        return render_template('map.html')
