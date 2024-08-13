import multiprocessing

import uvicorn
from app import app


def run_app():
    uvicorn.run(app, host=app.config['HOST'], port=app.config['PORT'])


if __name__ == '__main__':
    app_process = multiprocessing.Process(target=run_app)
    app_process.start()
    app_process.join()
