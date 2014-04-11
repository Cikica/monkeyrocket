does_mysql_exist="$(service mysql status)"

if [[ "mysql: unrecognized service" != "${does_mysql_exist}" ]]; then

	cp /vagrant/provision/init/mysql/files/mysql-config/my.cnf /etc/mysql/my.cnf
	cp /vagrant/provision/init/mysql/files/mysql-config/root-my.cnf /home/vagrant/.my.cnf

	# MySQL gives us an error if we restart a non running service, which
	# happens after a `vagrant halt`. Check to see if it's running before
	# deciding whether to start or restart.
	if [[ "mysql stop/waiting" == "${does_mysql_exist}" ]]; then
		service mysql start
	else
		service mysql restart
	fi

	mysql -u root -proot < /vagrant/provision/init/mysql/files/init.sql
	
else
	echo -e "\nMySQL is not installed. No databases imported."
fi