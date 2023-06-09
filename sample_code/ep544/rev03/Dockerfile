FROM ubuntu:jammy AS final
RUN --mount=type=secret,id=mysecret cat /run/secrets/mysecret
