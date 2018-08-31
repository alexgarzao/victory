# vagrant-xfce4-ubuntu

Vagrant-based development environment using [Ubuntu](https://xubuntu.org/), with GUI (i.e., not headless). The Xfce Desktop Environment is used instead of the default Unity for performance reasons.

The Vagrant base box is the official Ubuntu 16.04 (Xenial Xerus) 64-bit box [available from Hashicorp Atlas](https://atlas.hashicorp.com/ubuntu/boxes/xenial64).

## Installation

Prerequisites:

* [VirtualBox](https://www.virtualbox.org/wiki/Downloads). This has been tested with version 5.1.38
* [Vagrant](https://vagrantup.com/downloads.html). This has been tested using version 1.8.1

Clone this repository, then from the repository folder run this command:

    vagrant up

The `vagrant` user password is `vagrant`.

## Notes

* You can also SSH to the VM as user `vagrant`, using `vagrant ssh`
