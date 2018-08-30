#!/bin/bash

echo "Installing ODBC"
sudo DEBIAN_FRONTEND=noninteractive apt-get -qq install -y \
    unixodbc \
    unixodbc-dev
