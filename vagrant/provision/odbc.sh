#!/bin/bash

echo "Installing ODBC"
sudo DEBIAN_FRONTEND=noninteractive apt-get install -y \
    unixodbc \
    unixodbc-dev
