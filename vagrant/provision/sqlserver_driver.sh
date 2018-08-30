#!/bin/bash

# https://docs.microsoft.com/pt-br/sql/connect/odbc/linux-mac/installing-the-microsoft-odbc-driver-for-sql-server?view=sql-server-2017

echo "Installing Driver 17 SQL Server"
sudo su root -c "curl -s https://packages.microsoft.com/keys/microsoft.asc | apt-key add -"
sudo su root -c "curl -s https://packages.microsoft.com/config/ubuntu/16.04/prod.list > /etc/apt/sources.list.d/mssql-release.list"
sudo DEBIAN_FRONTEND=noninteractive apt-get update -y

sudo ACCEPT_EULA=Y DEBIAN_FRONTEND=noninteractive apt-get install -y \
    msodbcsql17 \
    mssql-tools \

echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bash_profile
echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bashrc
source ~/.bashrc

# optional: for unixODBC development headers
sudo DEBIAN_FRONTEND=noninteractive apt-get install -y \
    unixodbc-dev

sudo ACCEPT_EULA=Y DEBIAN_FRONTEND=noninteractive apt-get install -y \
    msodbcsql \
    mssql-tools
