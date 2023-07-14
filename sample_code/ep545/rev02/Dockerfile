FROM ubuntu:jammy

RUN : \
    && apt-get update \
    && apt-get install -y --no-install-recommends \
        locales \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN : \
    echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen && \
    locale-gen && \
    echo 'LANG="en_US.UTF-8"' >> /etc/default/locale && \
    echo
