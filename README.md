# REQUESTO project

## Description
REQUESTO is a tool for monitoring HTTP endpoints. It is a simple and easy to use tool for testing web applications. It is written in Python and uses the django rest framework.

## Installation & Running the project
Using docker-compose is the easiest way to run the project. You can find the docker-compose.yml file in the root of the project. You can run the project by running the following command:
```
docker-compose up
```
If you want to run the project without docker, you can follow the steps below:
1. Install the requirements by running the following command:
```
pip install -r requirements.txt
```
2. Run the following commands:
```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

## Usage
You can use the following endpoints to interact with the project:
1. POST /api/auth/login/ - Login user
2. POST /api/auth/register/ - Register user
3. POST /api/monitor/create/ - Create a new Monitoring endpoint (Authorization required)
4. GET /api/monitor/list/ - List all Monitoring endpoints (Authorization required)
5. GET /api/monitor/statistics/:id/ - Get statistics for a specific Monitoring endpoint (Authorization required)
6. GET /api/monitor/statistics/warnings/ - Get all warnings (Authorization required)


## Project structure
The project is divided into 3 main apps:
1. authentication app - Contains the authentication logic
2. Monitor app - Contains the monitoring logic
3. core app (requesto) - Contains the core logic of the project
