cp /vagrant/provision/init/php/files/php5-fpm.conf /etc/php5/fpm/php5-fpm.conf
cp /vagrant/provision/init/php/files/www.conf /etc/php5/fpm/pool.d/www.conf
cp /vagrant/provision/init/php/files/php-custom.ini /etc/php5/fpm/conf.d/php-custom.ini
cp /vagrant/provision/init/php/files/opcache.ini /etc/php5/fpm/conf.d/opcache.ini
cp /vagrant/provision/init/php/files/xdebug.ini /etc/php5/fpm/conf.d/xdebug.ini