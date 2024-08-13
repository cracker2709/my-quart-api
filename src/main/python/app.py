import os

import pkg_resources
from quart import Quart
from quart_cors import cors
from quart_schema import QuartSchema, Info

from api.async_routes import async_routes
from api.swagger import docs_routes

app = Quart(__name__)
cors(app, allow_origin="*")

# Initialize QuartSchema with proper info
schema_info = Info(title="My custom Quart API",
                   version=pkg_resources.get_distribution("my-quart-api").version,
                   description="Quart API")
schema = QuartSchema(app, info=schema_info)

app.config['HOST'] = os.getenv("SERVER_HOST")
app.config['PORT'] = int(os.getenv("SERVER_PORT", 5000))

# Register blueprints
app.register_blueprint(async_routes)
app.register_blueprint(docs_routes)
