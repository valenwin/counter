## Deploy project on your local machine

1 - To deploy project on your local machine create new virtual environment and execute this command:<br />

`pip install -r requirements.txt`

2 - Migrate db models to PostgreSQL:<br />
`python manage.py migrate`

3 - Run Redis server:<br />
`redis-server`

4 - Run app:<br />
`python manage.py runserver`