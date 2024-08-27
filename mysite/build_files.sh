
echo "BUILD START"

python3 -m venv .venv

source .venv/bin/activate

python3 -m pip install -r requirements.txt
python3 manage.py collectstatic --noinput

echo "BUILD END"