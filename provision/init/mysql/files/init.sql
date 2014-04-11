CREATE DATABASE IF NOT EXISTS `wordpress_default`;
GRANT ALL PRIVILEGES ON `wordpress_default`.* TO 'wp'@'localhost' IDENTIFIED BY 'wp';

GRANT ALL PRIVILEGES ON *.* TO 'external'@'%' IDENTIFIED BY 'external';