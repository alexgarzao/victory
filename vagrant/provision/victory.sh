#!/bin/bash

echo "Installing Victory"
sudo su vagrant
git clone https://github.com/alexgarzao/victory.git
cd victory
virtualenv -p python3.6 .env
. .env/bin/activate
pip -q install -r requirements.txt
cd victory; python setup.py install; cd ..

export LC_ALL=en_US.UTF-8
export LC_CTYPE=en_US.UTF-8

victory driverupdate
