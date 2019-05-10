FROM python:3.6-slim-stretch
RUN pip install -U pip
COPY ./app/requirements.txt .
RUN pip install -r requirements.txt
EXPOSE 5000
COPY ./app /app
WORKDIR /app
CMD ["python3", "main.py"]
