from flask import Flask
from app.api.routes import api


app = Flask(__name__, template_folder='./templates', static_folder='./static')
app.config.from_object('config')

app.register_blueprint(api, url_prefix='/')
