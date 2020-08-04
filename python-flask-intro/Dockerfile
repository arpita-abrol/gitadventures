FROM python:3.8.5-slim

WORKDIR /app

COPY Pipfile* /app/

RUN python3 -m pip install --upgrade pip \
  && python3 -m pip install --upgrade pipenv \
  && pipenv install --system --deploy

USER 1001

COPY . /app
ENV FLASK_APP=server/__init__.py
CMD ["python3", "manage.py", "start", "0.0.0.0:3000"]
