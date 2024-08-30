#!/bin/bash

echo "STARTING DEPLOYMENT"

# Activate the virtual environment
echo "Activating virtual environment..."
python -m venv .venv || exit 1
source .venv/bin/activate || exit 1

# Install dependencies
echo "Installing dependencies..."
python -m pip install -r requirements.txt || exit 1

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput || exit 1

echo "DEPLOYMENT SUCCESSFUL"
