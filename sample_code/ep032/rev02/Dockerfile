FROM ubuntu:focal

RUN : \
    && apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        ca-certificates \
        curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && :

RUN : \
    && curl --location --silent --output /go.tar.gz https://golang.org/dl/go1.14.3.linux-amd64.tar.gz \
    && echo '1c39eac4ae95781b066c144c58e45d6859652247f7515f0d2cba7be7d57d2226  /go.tar.gz' | sha256sum --check \
    && tar -xf /go.tar.gz \
    && rm /go.tar.gz \
    && :

# ADD https://golang.org/dl/go1.14.3.linux-amd64.tar.gz /go.tar.gz
# RUN tar -xf /go.tar.gz
