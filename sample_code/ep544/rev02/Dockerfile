FROM ubuntu:jammy AS builder
ARG SECRET
RUN echo $SECRET && echo hi > f
FROM ubuntu:jammy AS final
COPY --from=builder f .
