#!/bin/sh

apt-get update
apt-get install -y nginx

if [ ! -e /etc/nginx/server.key ]; then
	vvvgenrsa="$(openssl genrsa -out /etc/nginx/server.key 2048 2>&1)"
	echo $vvvgenrsa
fi

if [ ! -e /etc/nginx/server.csr ]; then
	openssl req -new -batch -key /etc/nginx/server.key -out /etc/nginx/server.csr
fi

if [ ! -e /etc/nginx/server.crt ]; then
	vvvsigncert="$(openssl x509 -req -days 365 -in /etc/nginx/server.csr -signkey /etc/nginx/server.key -out /etc/nginx/server.crt 2>&1)"
	echo $vvvsigncert
fi

cp $2/configuration/nginx.conf /etc/nginx/nginx.conf
cp $2/configuration/nginx-php.conf /etc/nginx/nginx-php.conf

if [ ! -d /etc/nginx/custom-sites ]; then
	mkdir /etc/nginx/custom-sites
fi

if [ $3 = "laravel" ]; then
	cp $2/configuration/laravel.conf /etc/nginx/custom-sites/laravel.conf
fi

if [ $3 = "wordpress" ]; then
	cp $2/configuration/laravel.conf /etc/nginx/custom-sites/wordpress.conf
fi