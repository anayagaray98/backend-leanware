FROM python:3

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

ADD ./requirements.txt /requirements.txt
RUN mkdir /backend
COPY ./backend /backend

WORKDIR /backend
ADD ./entrypoint.sh /

RUN set -ex \
    && pip install --upgrade pip  \ 
    && pip install -r /requirements.txt
ENTRYPOINT ["sh", "/entrypoint.sh"]
