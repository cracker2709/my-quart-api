from quart import Blueprint
import aiohttp
from quart_schema import tag

async_routes = Blueprint('async', __name__, url_prefix='/async')


@async_routes.route("/get/")
@tag(['Async Operations'])
async def get():
    async with aiohttp.ClientSession() as session:
        async with session.get('https://jsonplaceholder.typicode.com/todos/1') as response:
            data = await response.json()
            return data
