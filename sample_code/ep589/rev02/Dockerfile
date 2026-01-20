FROM ubuntu:jammy

RUN : \
    && apt-get update \
    && apt-get install -y --no-install-recommends \
        dumb-init \
        python3 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
