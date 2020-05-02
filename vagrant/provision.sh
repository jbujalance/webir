sudo apt-get install python3-venv -y
python3 -m venv ./venv
source venv/bin/activate
pip install gunicorn dist/webir-0.1.0-py3-none-any.whl