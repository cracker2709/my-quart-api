from quart import Blueprint, jsonify
from quart_schema import tag

health_routes = Blueprint('health', __name__, url_prefix='/health')


@health_routes.route("/")
@tag(['Health'])
async def health():
    return jsonify({"status": "ok"})
