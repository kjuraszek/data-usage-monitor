FROM python:3.9-slim-buster
RUN apt-get update && apt-get upgrade -y
RUN apt-get install libpq-dev build-essential -y
WORKDIR /code
COPY requirements.txt requirements.txt
ENV DOCKERIZED=true
ENV VIRTUAL_ENV=/opt/venv
RUN python3.9 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN pip install -r requirements.txt

COPY . .

CMD ["python3", "data_collector.py"]
