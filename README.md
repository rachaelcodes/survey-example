# pulse-survey-example

Example pulse survey for coding test - not a real project.

Before the technical test, ensure you have cloned the repo, and have made a copy in your

## Summary

The Cabinet Office are running a pulse survey to understand staff wellbeing. Cabinet Office employees will be asked to complete this survey.

- Staff details will not be submitted with their survey responses (session ID will be stored to distinguish participants)
- Collect info on team and location, in addition to answers to wellbeing questions
- Separately to survey responses, staff can enter feedback and email if they wish to discuss issues more

This is a Django app with a SQLite database.

## How to run with Docker

- Run the app locally `docker-compose up --build`
- Go to `http://localhost:8000` in a browser to try the app

## How to run without Docker

- Install packages with `pip install -r requirements.lock` (ideally into a virtual environment)
- Run migrations `python manage.py migrate` (only need to do this once, or if you make changes to models)
- Run the app locally `python manage.py runserver`
- Go to `http://localhost:8000` in the browser to try the app

This has been tested using Python 3.8.
