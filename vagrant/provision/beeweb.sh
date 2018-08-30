#!/bin/bash

echo "Installing beeweb"
sudo su vagrant
git clone https://github.com/alexgarzao/beeweb.git
cd beeweb
virtualenv -p python3.6 .env
. .env/bin/activate
pip -q install -r requirements.txt
pip -q install --editable cli/.

export LC_ALL=en_US.UTF-8
export LC_CTYPE=en_US.UTF-8

python cli/webdriver_download/webdriver.py update
