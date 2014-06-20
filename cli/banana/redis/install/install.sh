#!/bin/sh

cd /usr/local/src
wget http://download.redis.io/releases/redis-2.8.9.tar.gz
tar xzvf redis-2.8.9.tar.gz

cd redis-2.8.9
make

rm /usr/local/src/redis-2.8.9.tar.gz

cp src/redis-server /usr/local/bin
cp src/redis-cli /usr/local/bin

mkdir /etc/redis
mkdir /var/redis
mkdir /var/redis/$4

cp $5 /etc/init.d/redis_$3
cp $6 /etc/redis/$3.conf
rm $5
rm $6

update-rc.d redis_$3 defaults

/etc/init.d/redis_$3 start