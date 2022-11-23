FROM python:3.7-slim
WORKDIR /app
COPY . .
RUN pip3 install --upgrade pip
RUN ls backend/
RUN ls backend/foodgram
RUN pip3 install -r backend/foodgram/requirements.txt --no-cache-dir
COPY . .
CMD ["gunicorn", "backend.foodgram.foodgram.wsgi:application", "--bind", "0:8000"]