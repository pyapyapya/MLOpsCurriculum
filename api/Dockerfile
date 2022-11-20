FROM python:3.9.10

WORKDIR /app

COPY ./requirements.txt /app

RUN pip install --upgrade -r /app/requirements.txt

COPY ./app /app

CMD ["uvicorn", "main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "80"]
