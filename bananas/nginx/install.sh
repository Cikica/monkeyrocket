#!/bin/sh

# apt-get update
# apt-get install nginx
# apt-get clean

if [ $1 = "php" ]; then
	cp /vagrant/bananas/nginx/configuration_files/php/nginx.conf /etc/nginx/nginx.conf
	cp /vagrant/bananas/nginx/configuration_files/php/nginx-common.conf /etc/nginx/nginx-common.conf
fi

if [ ! -d /etc/nginx/custom-sites ]; then
	mkdir /etc/nginx/custom-sites
fi