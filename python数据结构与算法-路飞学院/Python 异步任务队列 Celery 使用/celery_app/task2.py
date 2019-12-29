import time
from celery_app import app


@app.task
def multiply(x, y):
    print('Enter call function ...')
    time.sleep(4)
    return x * y