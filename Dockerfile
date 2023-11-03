FROM python:3.10

WORKDIR /app

COPY ./tesis /chatgpt/
COPY ./venv /app/venv

RUN pip install -r /app/requirements.txt

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]