FROM python:3.8

ENV WAIT_VERSION 2.9.0
ENV PYTHONUNBUFFERED=1
ENV FLASK_DEBUG=1 

ADD https://github.com/ufoscout/docker-compose-wait/releases/download/$WAIT_VERSION/wait /usr/local/bin/wait

COPY requirements-dev.txt /code/requirements-dev.txt
COPY infrastructure/entrypoint.sh /usr/bin/start.sh

WORKDIR /code

RUN chmod a+x /usr/local/bin/wait
RUN chmod a+x /usr/bin/start.sh
RUN pip install -r requirements-dev.txt

ENTRYPOINT [ "/usr/bin/start.sh" ]