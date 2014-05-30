#!/bin/sh

# apt-get update
# apt-get install -y nginx 
# apt-get install -y php5
# apt-get install -y php5-fpm
# apt-get install -y php5-json
# apt-get install -y php5-mysql
# apt-get install -y php5-fpm
# apt-get install -y php5-cli
# apt-get install -y php5-common
# apt-get install -y php5-dev
# apt-get install -y php5-memcache
# apt-get install -y php5-imagick
# apt-get install -y php5-xdebug
# apt-get install -y php5-mcrypt
# apt-get install -y php5-mysql
# apt-get install -y php5-imap
# apt-get install -y php5-curl
# apt-get install -y php-pear
# apt-get install -y php5-gd
# apt-get install -y unzip
# apt-get install -y git
# apt-get clean

# cd /etc/php5/mods-available/
# php5enmod mcrypt

# cd $1

# curl -sS https://getcomposer.org/installer | php
# mv $1/composer.phar /usr/local/bin/composer

# if [ ! -d /vagrant/main/laravel ]; then
# 	wget https://github.com/laravel/laravel/archive/master.zip
# 	unzip master.zip -d /vagrant/main
# 	rm master.zip
# 	mv /vagrant/main/laravel-master /vagrant/main/laravel
# 	cd /vagrant/main/laravel
# 	composer install
# fi

# if [ ! -e /etc/nginx/server.key ]; then
# 	vvvgenrsa="$(openssl genrsa -out /etc/nginx/server.key 2048 2>&1)"
# 	echo $vvvgenrsa
# fi

# if [ ! -e /etc/nginx/server.csr ]; then
# 	openssl req -new -batch -key /etc/nginx/server.key -out /etc/nginx/server.csr
# fi

# if [ ! -e /etc/nginx/server.crt ]; then
# 	vvvsigncert="$(openssl x509 -req -days 365 -in /etc/nginx/server.csr -signkey /etc/nginx/server.key -out /etc/nginx/server.crt 2>&1)"
# 	echo $vvvsigncert
# fi

# cp $1/banana/laravel/configuration_files/php/nginx.conf /etc/nginx/nginx.conf
# cp $1/banana/laravel/configuration_files/php/nginx-common.conf /etc/nginx/nginx-common.conf
# if [ ! -d /etc/nginx/custom-sites ]; then
# 	mkdir /etc/nginx/custom-sites
# fi
# cp $1/banana/laravel/configuration_files/php/laravel.conf /etc/nginx/custom-sites/laravel.conf

# Installing redis
cd /usr/local/src
# wget http://download.redis.io/releases/redis-2.8.9.tar.gz
# tar xzvf redis-2.8.9.tar.gz
# cd redis-2.8.9

# make
# rm /usr/local/src/redis-2.8.9.tar.gz

cp src/redis-server /usr/local/bin
cp src/redis-cli /usr/local/bin

mkdir /etc/redis
mkdir /var/redis
mkdir /var/redis/6379
cp $2/configuration_files/redis_6379 /etc/init.d/redis_6379
cp $2/configuration_files/redis.conf /etc/redis/6379.conf
update-rc.d redis_6379 defaults

/etc/init.d/redis_6379 start