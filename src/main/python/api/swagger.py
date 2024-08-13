from quart import Blueprint
from quart_schema import QuartSchema

docs_routes = Blueprint('docs_routes', __name__)
schema = QuartSchema()


@docs_routes.route("/swagger")
async def docs():
    return await schema.swagger_ui()
