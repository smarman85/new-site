FROM smarman/alp_py37

ADD reqs.txt uwsgi.ini /etc/
ADD app /srv

WORKDIR /srv

RUN apk add --no-cache --virtual \
    .build-deps \
    gcc \
    python3-dev \
    build-base \
    linux-headers && \
    addgroup -S webuser && adduser -S webuser -G webuser && \
    python3.7 -m venv /etc/venv && source /etc/venv/bin/activate && \
    pip install --upgrade pip && \
    pip install -r /etc/reqs.txt && \
    apk del .build-deps

USER webuser

CMD ["/etc/venv/bin/uwsgi", "--ini", "/etc/uwsgi.ini"]
