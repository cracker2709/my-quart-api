import os

import aiohttp
from quart import Quart
from quart_cors import cors
from quart_schema import QuartSchema

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


@app.route('/')
async def hello():
    return 'Hello, Quart!'


@app.route("/async")
async def get():
    async with aiohttp.ClientSession() as session:
        async with session.get('https://jsonplaceholder.typicode.com/todos/1') as response:
            data = await response.json()
            return data



# Add a route to serve the Swagger UI
@app.route("/docs")
async def docs():
    return await QuartSchema.swagger_ui()
