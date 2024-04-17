PYTHONPATH=`pwd`/src
uvicorn src.app:app --port 8000
# gunicorn -w 4 -k uvicorn.workers.UvicornWorker app:app
