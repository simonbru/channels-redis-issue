FROM python:3.7-buster

RUN apt-get update -y && apt-get install -y git lsof

COPY requirements.txt .
RUN pip install -r requirements.txt


# Override version of channels_redis:

# Last working commit
# RUN pip install https://github.com/django/channels_redis/archive/38ffdeb610ce175a01698ca267a6cccc171043c9.zip

# First commit with leak
# RUN pip install https://github.com/django/channels_redis/archive/3656d87813d643bee28fe1960124063268c850a2.zip