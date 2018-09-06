# PARA FAZER O BUILD: docker build --force-rm -t beeweb .
# PARA RODAR: docker run -e "FEATURES_PATH=samples/google-search" beeweb

FROM python:3.6-alpine

ENV PYTHONUNBUFFERED 1

COPY behave.ini /
COPY requirements.txt /
COPY cli /cli
COPY features /
COPY samples /

RUN apk add --no-cache --virtual .pynacl_deps build-base python3-dev libffi-dev libressl-dev unixodbc unixodbc-dev
RUN pip install -r requirements.txt
RUN cd cli && python setup.py install && cd ..
RUN beeweb driverupdate

CMD beeweb run $FEATURES_PATH
