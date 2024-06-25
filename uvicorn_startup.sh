#!/bin/sh

export APP_MODULE=${APP_MODULE-src.app.main:app}
export HOST=${HOST:-0.0.0.0}
export PORT=${PORT:-8000}
export PYTHONPATH=$PYTHONPATH:$(pwd)/src:$(pwd)/src/app

exec uvicorn --host $HOST --port $PORT "$APP_MODULE" --log-level debug
