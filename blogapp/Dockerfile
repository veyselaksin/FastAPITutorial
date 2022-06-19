FROM ubuntu:20.04

COPY ./requirements.txt /requirements.txt
COPY ./app /app

WORKDIR /app

RUN apt update -y && apt upgrade -y &&\
    apt install python3 python3-dev python3-pip python3-venv -y && \
    python3 -m venv venv && venv/bin/pip install --upgrade pip

RUN pip --no-cache-dir install -r /requirements.txt

ENV PATH="/app:venv/bin:$PATH"

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]