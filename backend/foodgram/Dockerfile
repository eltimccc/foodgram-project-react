FROM python:3.7-slim
RUN ls
WORKDIR /app
RUN ls
COPY backend/foodgram/requirements.txt .
RUN pip3 install -r requirements.txt --no-cache-dir
RUN ls
COPY . .
RUN ls
CMD ["gunicorn", "backend.foodgram.foodgram.wsgi:application", "--bind", "0:8000" ]