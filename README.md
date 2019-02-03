# Project 6: Mineral Catalog

Task: Build a website that displays information about various minerals (AKA rocks). The home page of the site contains a list of all of the minerals in a database. Clicking on a mineral’s name opens a page that displays information about the mineral.

## Dependencies

* Python 3.6 or later
* Django 1.11 LTS

Refer to requirements.txt

## To start

### 1. Initialize virtual environment to run the project

```
git clone https://github.com/nauticalist/django_mineralcatalog.git
cd django_mineralcatalog
python3 -m venv .env
source .env/bin/activate
pip install -r requirements.txt
python manage.py migrate
```

### 2. Load fixtures to database

Enter the python shell with:
```
python manage.py shell
```
Load the fixtures data
```python
from load_fixtures import load_data

load_data()
```
Press CTRL + D to exit


