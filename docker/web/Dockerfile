FROM ubuntu

WORKDIR /web


# For using javascript libraries with bower

RUN apt-get update && apt-get install -y build-essential
RUN apt-get update && apt-get install -y curl
RUN apt-get update && apt-get install -y git-core
RUN curl -sL https://deb.nodesource.com/setup_10.x | bash - \
    && apt-get install -y nodejs \
    && npm install -g bower
