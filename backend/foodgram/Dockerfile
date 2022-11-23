FROM python:3.7-slim
WORKDIR /app
COPY backend/ .
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt --no-cache-dir
COPY . .
RUN ls
RUN ls foodgram/
RUN ls backend/
RUN pwd
CMD ["gunicorn", "foodgram.wsgi:application", "--bind", "0:8000"]