#!/bin/sh

apt-get update
apt-get install -y php5
apt-get install -y php5-fpm
apt-get install -y php5-json
apt-get install -y php5-mysql
apt-get install -y php5-fpm
apt-get install -y php5-cli
apt-get install -y php5-common
apt-get install -y php5-dev
apt-get install -y php5-memcache
apt-get install -y php5-imagick
apt-get install -y php5-xdebug
apt-get install -y php5-mcrypt
apt-get install -y php5-mysql
apt-get install -y php5-imap
apt-get install -y php5-curl
apt-get install -y php-pear
apt-get install -y php5-gd

cd /etc/php5/mods-available/
php5enmod mcrypt

cd $1

curl -sS https://getcomposer.org/installer | php
mv $1/composer.phar /usr/local/bin/composer