#!/bin/bash

echo "Installing base"

sudo DEBIAN_FRONTEND=noninteractive apt-get -y update
sudo DEBIAN_FRONTEND=noninteractive apt-get -y upgrade

echo "export LC_ALL=en_US.UTF-8" >> ~/.bashrc
echo "export LC_CTYPE=en_US.UTF-8" >> ~/.bashrc
source ~/.bashrc

sudo su root -c 'echo "LANG=en_US.UTF-8" >> /etc/environment'
sudo su root -c 'echo "LANGUAGE=en_US.UTF-8" >> /etc/environment'
sudo su root -c 'echo "LC_ALL=en_US.UTF-8" >> /etc/environment'
sudo su root -c 'echo "LC_CTYPE=en_US.UTF-8" >> /etc/environment'
