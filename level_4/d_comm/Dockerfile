FROM python:3.7-slim

RUN pip3 install --upgrade pip setuptools wheel

# for installing curl, handy for testing
RUN apt-get update && apt-get install -y curl && apt-get clean

# for installing uwsgi, we have to install C compiler
RUN apt-get --assume-yes install gcc

# install dependencies
ADD requirements.txt .
RUN pip3 install -r requirements.txt

WORKDIR /opt/workdir

CMD ["bash", "entry.sh"]
