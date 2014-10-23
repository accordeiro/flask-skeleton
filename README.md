Flask-Skeleton
======================

## Getting started
1. Create your virtual environment inside project's root:
`$ cd /path/to/repo/ && virtualenv venv`

2. Activate your virtualenv:
`$ . /venv/bin/activate`

3. Install the requirements:
`$ pip install -r requirements.txt`

4. If you're an unfortunate Ubuntu user who can't get pip to install psycopg2, please run this:
`$ sudo apt-get install build-essential && sudo apt-get build-dep python-psycopg2 && pip install -r requirements.txt`

5. Set up Postgres:
`$ brew install postgresql`

6. Configure your .env file. An example has been set up for you:
`$ cp env.example .env`

7. Sync your database:
`$ python manage db upgrade`

8. Install [Heroku's Toolbelt](https://devcenter.heroku.com/articles/getting-started-with-python#set-up).

9. Run the app:
`$ python run.py`

## Scraping tool
1. Install dependencies:
`$ cd /path/to/repo/scraper && npm install`

2. Run the tool:
`$ cd /path/to/repo/ && mkdir -p data/json && mkdir -p data/csv && bash batch.sh`


flask-skeleton
==============

$ virtualenv venv
$ . venv/bin/activate
$ pip install -r requirements.txt
$ python manage db upgrade
$ python manage create_admin foo@bar.com password
