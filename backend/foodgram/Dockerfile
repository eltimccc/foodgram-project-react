FROM python:3.7-slim
WORKDIR /app
COPY backend/ .
RUN pip3 install --upgrade pip
RUN ls
RUN pip3 install -r foodgram/requirements.txt --no-cache-dir
COPY . .
CMD ["gunicorn", "foodgram.foodgram.wsgi:application", "--bind", "0:8000"]