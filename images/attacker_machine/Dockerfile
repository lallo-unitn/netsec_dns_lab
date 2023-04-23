FROM alpine:latest
LABEL maintainer="development@cicirello.org" \
    org.opencontainers.image.description="A lightweight docker image for shell scripting with GNU tools including bash, coreutils, findutils, and gawk." \
    org.opencontainers.image.authors="Vincent A Cicirello, development@cicirello.org, https://www.cicirello.org/" \
    org.opencontainers.image.source="https://github.com/cicirello/gnu-on-alpine" \
    org.opencontainers.image.title="gnu-on-alpine" 
RUN apk --no-cache add \
    bash \
    coreutils \
    findutils \
    gawk
