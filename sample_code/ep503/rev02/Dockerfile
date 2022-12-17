FROM ubuntu:jammy AS builder

RUN : \
    && apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        gcc \
        libc6-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY main.c .
RUN gcc -o /usr/local/bin/hello-hello-world main.c

FROM ubuntu:jammy AS final

COPY --from=builder /usr/local/bin/hello-hello-world /usr/local/bin/
