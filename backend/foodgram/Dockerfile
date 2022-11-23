FROM python:3.7-slim
WORKDIR /app/backend/foodgram/
COPY /backend/foodgram/requirements.txt .
RUN pip3 install --upgrade pip --no-cache-dir
RUN pip3 install -r requirements.txt --no-cache-dir
COPY . .
RUN ls
RUN pwd
CMD ["gunicorn", "foodgram.wsgi:application", "--bind", "0:8000"]