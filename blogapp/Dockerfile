FROM ubuntu:20.04

LABEL maintainer="veyselaksin"
ENV PYTHONUNBUFFERED=1

COPY ./requirements.txt /home/blogapp/requirements.txt
COPY ./app /home/blogapp/app

WORKDIR /home/blogapp

RUN apt update -y && apt upgrade -y &&\
    apt install python3 build-essential libpq-dev python3-dev python3-pip python3-venv -y && \
    python3 -m venv venv && venv/bin/pip install --upgrade pip

RUN pip --no-cache-dir install -r /home/blogapp/requirements.txt

ENV PATH="/app:venv/bin:$PATH"

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]