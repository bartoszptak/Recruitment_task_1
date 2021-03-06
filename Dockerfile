FROM python:3.6-slim-stretch

RUN apt-get update && \
    apt-get install -y --no-install-recommends make gcc g++ && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN pip install -U pip
COPY ./app/requirements.txt .
RUN pip install -r requirements.txt
EXPOSE 5000
COPY ./app /app
WORKDIR /app
CMD ["python3", "main.py"]
