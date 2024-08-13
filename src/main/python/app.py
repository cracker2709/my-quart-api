import os

import aiohttp
from quart import Quart
from quart_cors import cors
from quart_schema import QuartSchema

from api import async_routes
from api.swagger import docs_routes

app = Quart(__name__)
cors(app, allow_origin="*")
info = dict()
info['title'] = "Quart API"
info['version'] = "1.0"
schema = QuartSchema(app)
schema.title = "Quart API"
schema.description = "Quart API"
schema.version = "1.0"
app.config['HOST'] = os.getenv("SERVER_HOST")
app.config['PORT'] = int(os.getenv("SERVER_PORT", 5000))


# Register blueprints
app.register_blueprint(async_routes)
app.register_blueprint(docs_routes)

info = dict()
info['title'] = "Quart API"
info['version'] = "1.0"