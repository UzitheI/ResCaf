#!/bin/bash
set -e
set -x

# Activate virtual environment if you're using one
# source /path/to/your/venv/bin/activate

pip install -r requirements.txt
python manage.py collectstatic --noinput