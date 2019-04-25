FROM ubuntu:latest as base

LABEL maintainer="Ben Sachs <sachsbl@gmail.com>"

# See http://bugs.python.org/issue19846
ENV LANG C.UTF-8

RUN apt-get update
RUN apt-get install -y python3 python3-dev python3-pip

RUN pip3 --no-cache-dir install --upgrade pip setuptools

# install web server
RUN pip3 install gunicorn

COPY ./ ./app
WORKDIR ./app

RUN chmod +x run_server.sh

# Some TF tools expect a "python" binary
RUN ln -s $(which python3) /usr/local/bin/python

RUN pip3 install -r requirements.txt

EXPOSE 5000
ENTRYPOINT ["./run_server.sh"]
