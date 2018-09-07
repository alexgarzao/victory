# PARA FAZER O BUILD: docker build --force-rm -t beeweb .
# PARA RODAR: docker run -e "FEATURES_PATH=samples/google-search" beeweb

FROM python:3.6-alpine

ENV PYTHONUNBUFFERED 1

RUN apk update
RUN apk upgrade
RUN apk add --no-cache --virtual .pynacl_deps build-base python3-dev libffi-dev libressl-dev unixodbc unixodbc-dev

# install chromedriver (instead of beeweb driverupdate)
RUN apk add chromium chromium-chromedriver

# Install APP
WORKDIR /app
COPY behave.ini /app
COPY requirements.txt /app
COPY cli /app/cli
COPY features /app/features
COPY samples /app/samples
RUN pip install -r requirements.txt
RUN cd cli && python setup.py install && cd ..

CMD beeweb run $FEATURES_PATH
