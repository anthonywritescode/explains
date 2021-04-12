FROM ubuntu:focal

RUN : \
    && apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y \
        --no-install-recommends \
        libglib2.0-0 \
        python3-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && :
