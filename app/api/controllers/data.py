from flask.views import MethodView


class DataController(MethodView):
    def get(self):
        with open('DataAnalysis/data/coords.json', 'r', encoding='utf-8') as input:
            coords = input.read()
        return coords
