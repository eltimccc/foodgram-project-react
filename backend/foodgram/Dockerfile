FROM python:3.7-slim
WORKDIR /backend/foodgram/
COPY /backend/foodgram/requirements.txt .
RUN pip install --upgrade pip --no-cache-dir
RUN apt-get update
RUN pip install psycopg2-binary
RUN pip install -r ./requirements.txt --no-cache-dir
COPY . .
CMD ["gunicorn", "config.wsgi:application", "--bind", "0:8000"]