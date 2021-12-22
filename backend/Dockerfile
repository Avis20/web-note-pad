# (1)
FROM python:3.9-buster

# (2)
WORKDIR /app

# (3)
ENV PYTHONUNBUFFERED 1

# (4)
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# (5)
COPY ./src .
