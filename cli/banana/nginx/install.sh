#!/bin/sh

apt-get update
apt-get install nginx
apt-get clean

cp /vagrant/bananas/nginx/configuration_files/php/nginx.conf /etc/nginx/nginx.conf
cp /vagrant/bananas/nginx/configuration_files/php/nginx-common.conf /etc/nginx/nginx-common.conf

mkdir /etc/nginx/custom-sites