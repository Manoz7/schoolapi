FROM python:3.8-slim
ENV PYTHONUNBUFFERED=1
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN apt update && apt install build-essential -y
RUN pip install -r requirements.txt