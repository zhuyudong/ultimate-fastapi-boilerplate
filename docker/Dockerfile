# pull official base image
FROM python:3.11-slim-buster

ENV TZ=Asia/Shanghai
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ >/etc/timezone

# set working directory
# WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies, postgresql
RUN sed -i 's|deb.debian.org|mirrors.ustc.edu.cn|g' /etc/apt/sources.list \
  && sed -i 's|security.debian.org|mirrors.ustc.edu.cn|g' /etc/apt/sources.list \
  && apt-get update \
  && apt-get -y install netcat gcc \
  && apt-get clean

# install python dependencies
# WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv
RUN pip install --upgrade pip -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com
COPY ./requirements/base.txt .

# RUN poetry install
RUN pip install -r base.txt -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com

# add app
COPY . .
EXPOSE 8000

CMD sh uvicorn_startup.sh
# CMD sh gunicorn_startup.sh
