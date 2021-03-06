#!/bin/sh


set -o errexit
set -o nounset


celery worker --app=celery_app.app:app -lINFO --concurrency=1 -Ofair --pool=eventlet --hostname=worker@%h


exec "$@"
