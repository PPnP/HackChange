from flask import Blueprint

api = Blueprint('api', __name__, template_folder='../templates', static_folder='../static')


from app.api.controllers.index import IndexPageController
api.add_url_rule('/', view_func=IndexPageController.as_view('IndexPage'))

from app.api.controllers.map import MapController
api.add_url_rule('/map', view_func=MapController.as_view('Map'))
