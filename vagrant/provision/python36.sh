#!/bin/bash

echo "Installing Python 3.6"
sudo DEBIAN_FRONTEND=noninteractive add-apt-repository -y ppa:jonathonf/python-3.6
sudo DEBIAN_FRONTEND=noninteractive apt-get -qq update -y
sudo DEBIAN_FRONTEND=noninteractive apt-get -qq install -y \
    python3.6 \
    python3.6-dev \
    python-pip

sudo DEBIAN_FRONTEND=noninteractive -H pip -q install --upgrade pip
sudo DEBIAN_FRONTEND=noninteractive -H pip -q install virtualenv
