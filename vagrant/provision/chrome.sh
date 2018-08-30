#!/bin/bash

echo "Installing Chrome"
sudo wget -q https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo DEBIAN_FRONTEND=noninteractive apt-get -qq install -y \
    ./google-chrome-stable_current_amd64.deb
sudo rm ./google-chrome-stable_current_amd64.deb
