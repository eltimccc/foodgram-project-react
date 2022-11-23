FROM python:3.7-slim
WORKDIR /app
COPY requirements.txt .
# COPY backend/ .
RUN pip3 install -r requirements.txt
COPY . .
RUN pip3 install -r foodgram/requirements.txt --no-cache-dir
RUN ls
RUN pwd
CMD ["gunicorn", "foodgram.wsgi:application", "--bind", "0:8000"]