FROM python:3.7-slim-stretch

RUN apt-get update -y && apt-get install -y libzbar-dev bash gcc git libc-dev curl wget vim nano \
    && apt-get install -y ranger caca-utils highlight atool w3m poppler-utils mediainfo \
    && apt-get install -y iputils-ping telnet openssh-client net-tools \
    man unzip vim-tiny bc openssh-server thrift-compiler netcat sudo \
    && apt-get install -y build-essential \
    && apt-get autoremove -y \
    && apt-get clean

#Project
RUN apt-get update && apt-get install -y libgl1-mesa-glx 'ffmpeg' 'libsm6' 'libxext6'

RUN pip install --upgrade pip

COPY dockers/app/requirements/base.txt base.txt
RUN pip install --no-cache-dir -r base.txt \
    && rm -rf base.txt

RUN mkdir -p /main
# COPY ./src /main

RUN chmod -R 777 /main
WORKDIR /main
