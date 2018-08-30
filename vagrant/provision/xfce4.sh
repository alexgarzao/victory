#!/bin/bash

echo "Installing XFCE"
sudo DEBIAN_FRONTEND=noninteractive apt-get -qq install -y\
    xfce4 \
    virtualbox-guest-dkms \
    virtualbox-guest-utils \
    virtualbox-guest-x11 \
    xserver-xorg-legacy

sudo VBoxClient --clipboard
sudo VBoxClient --draganddrop
sudo VBoxClient --display
sudo VBoxClient --checkhostversion
sudo VBoxClient --seamless

sudo chmod ug+s /usr/lib/xorg/Xorg

sudo su -c 'echo "allowed_users=anybody" > /etc/X11/Xwrapper.config'

# echo "startxfce4 &" >> ~/.bashrc
