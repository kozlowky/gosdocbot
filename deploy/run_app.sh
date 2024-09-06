#!/bin/bash

python "manage.py" collectstatic --noinput
python "manage.py" migrate --noinput
python "manage.py" runserver 0.0.0.0:8000 &
python "manage.py" run_bot

gunicorn -c "$PROJECT_ROOT/gunicorn.conf.py" server.wsgi:application

