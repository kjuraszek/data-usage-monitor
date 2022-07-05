FROM python:3.9-slim-buster
RUN apt-get update && apt-get upgrade -y
RUN apt-get install libpq-dev build-essential -y
WORKDIR /code
RUN mkdir backend
COPY requirements.txt backend/requirements.txt
ENV DOCKERIZED=true
ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN pip install -r backend/requirements.txt

COPY . backend

EXPOSE 5000

RUN chmod +x backend/entrypoint.sh
ENTRYPOINT ["backend/entrypoint.sh"]
