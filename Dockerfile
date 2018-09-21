# PARA FAZER O BUILD: docker build --force-rm -t victory .
# PARA RODAR: docker run -e "MODULE=web" -e "FEATURES_PATH=samples/google-search" victory

# PARA publicar no docker hub: docker login; docker tag victory alexgarzao/victory; docker push alexgarzao/victory
# PARA RODAR: docker run -e "MODULE=web" -e "FEATURES_PATH=samples/google-search" alexgarzao/victory

FROM python:3.6-alpine

ENV PYTHONUNBUFFERED 1

RUN apk update
RUN apk upgrade
RUN apk add --no-cache --virtual .pynacl_deps build-base python3-dev libffi-dev libressl-dev unixodbc unixodbc-dev

# install chromedriver (instead of victory driverupdate)
RUN apk add chromium chromium-chromedriver

# Install APP
WORKDIR /app
COPY behave.ini /app
COPY requirements.txt /app
COPY victory /app/victory
COPY features /app/features
COPY web_features /app/web_features
COPY api_features /app/api_features
COPY samples /app/samples
RUN pip install -r requirements.txt
RUN cd victory && python setup.py install && cd ..

CMD victory run --headless $MODULE $FEATURES_PATH
