if [[ ! -d /vagrant/main/default ]]; then

	cd /vagrant/main

	curl -L https://raw.github.com/wp-cli/builds/gh-pages/phar/wp-cli.phar > wp-cli.phar
	chmod +x wp-cli.phar
	ln -sf /vagrant/main/wp-cli.phar /usr/local/bin/wp

	curl -O http://wordpress.org/latest.tar.gz
	tar -xvf latest.tar.gz
	mv wordpress default
	rm latest.tar.gz
	cd /vagrant/main/default
	wp core config --dbname=wordpress_default --dbuser=wp --dbpass=wp --quiet --extra-php --allow-root <<PHP
define( 'WP_DEBUG', true );
PHP
	wp core install --url=local.wordpress.dev --quiet --title="Local WordPress Dev" --admin_name=admin --admin_email="admin@local.dev" --admin_password="password" --allow-root 
fi