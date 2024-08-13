import pkg_resources
from quart import Blueprint
from quart_schema import QuartSchema, Info

docs_routes = Blueprint('docs_routes', __name__, url_prefix='/api/v1')
schema_info = Info(title="My custom Quart API",
                   version=pkg_resources.get_distribution("my-quart-api").version,
                   description="Quart API")
schema = QuartSchema(info=schema_info)


@docs_routes.route("/")
async def docs():
    return await schema.swagger_ui()
