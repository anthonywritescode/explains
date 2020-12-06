FROM ubuntu:focal

# ...

RUN : \
    && virtualenv /venv -p python3 \
    && /venv/bin/pip install -r requirements.txt \
    && /venv/bin/pip install -r requirements-dev.txt \
    && :

RUN virtualenv /venv -p python3 && \
    /venv/bin/pip install -r requirements.txt && \
    /venv/bin/pip install -r requirements-dev.txt
