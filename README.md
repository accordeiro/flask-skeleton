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

8. Create an admin user:
`$ python manage create_admin <email> <password>`

9. Run your app:
`$ python run`

10. Access your admin interface at http://localhost:5000
