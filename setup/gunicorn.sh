#!/bin/bash
NAME="gunicorn"
ROOTDIR=/automatic-test-generator/

NUM_WORKERS=1

cd $ROOTDIR
pwd
exec gunicorn app:app \
    --name $NAME \
    --workers $NUM_WORKERS \
    --bind=0.0.0.0:80 \
    --worker-class=gevent \
    --worker-connections=100 \
    --log-level=info \
    --access-logfile=- \
    --timeout=120 \
    --reload
