FROM python:3.9.1
RUN echo exit 0 > /usr/sbin/policy-rc.d
RUN /usr/local/bin/python -m pip install --upgrade pip
WORKDIR /usr/src/app
RUN pip install mysql-connector-python
COPY . .
RUN apt-get update
RUN apt-get -y install default-mysql-client