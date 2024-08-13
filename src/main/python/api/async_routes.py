from quart import Blueprint
import aiohttp

async_routes = Blueprint('async_namespace', __name__, url_prefix='/api/v1/async_ns')


@async_routes.route("/async")
async def get():
    async with aiohttp.ClientSession() as session:
        async with session.get('https://jsonplaceholder.typicode.com/todos/1') as response:
            data = await response.json()
            return data
