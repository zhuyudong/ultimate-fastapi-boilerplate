export PYTHONPATH=$PYTHONPATH:$(pwd)/src:$(pwd)/src/app

gunicorn --workers 8 --threads 4 --timeout 60 --access-logfile \
    '-' --error-logfile '-' --bind=0.0.0.0:8000 -k uvicorn.workers.UvicornWorker \
    --chdir=./ src.app.main:app
