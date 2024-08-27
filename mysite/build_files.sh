ECHO 'START'

python -m venv .venv
source .venv/bin/activate

python -m pip install -r requirements.txt 
python manage.py collectstatic --noinput

ECHO 'END'