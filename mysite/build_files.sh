#!/bin/bash

echo "BUILD START"

# Create and activate the virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
python -m pip install --upgrade pip  # Upgrade pip to avoid potential issues
python -m pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --noinput

echo "BUILD END"
