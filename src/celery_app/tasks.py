import os
import logging
from datetime import datetime

import time
import requests
import tempfile


from celery import current_task
from .app import app as celery_app

# logging
LOGS_DIR = os.getenv("LOGS_DIR")
os.makedirs(LOGS_DIR, exist_ok=True)

file_name = str(datetime.now().strftime("%d_%m_%Y")) + ".log"
logging.basicConfig(
    filename=LOGS_DIR + file_name,
    level=logging.INFO,
    format="%(asctime)s | {%(pathname)s:%(lineno)d} | %(module)s | %(levelname)s | %(funcName)s | %(message)s"
)