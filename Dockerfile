# PARA FAZER O BUILD: docker build --force-rm -t beeweb .
# PARA RODAR: docker run -e "MODULE=web" -e "FEATURES_PATH=samples/google-search" beeweb

# PARA publicar no docker hub: docker login; docker tag beeweb alexgarzao/beeweb; docker push alexgarzao/beeweb
# PARA RODAR: docker run -e "MODULE=web" -e "FEATURES_PATH=samples/google-search" alexgarzao/beeweb

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
COPY beeweb /app/beeweb
COPY features /app/features
COPY web_features /app/web_features
COPY api_features /app/api_features
COPY samples /app/samples
RUN pip install -r requirements.txt
RUN cd beeweb && python setup.py install && cd ..

CMD beeweb run --headless $MODULE $FEATURES_PATH
