if [[ ! -e /etc/nginx/server.key ]]; then
	echo "Generate Nginx server private key..."
	vvvgenrsa="$(openssl genrsa -out /etc/nginx/server.key 2048 2>&1)"
	echo $vvvgenrsa
fi
if [[ ! -e /etc/nginx/server.csr ]]; then
	echo "Generate Certificate Signing Request (CSR)..."
	openssl req -new -batch -key /etc/nginx/server.key -out /etc/nginx/server.csr
fi
if [[ ! -e /etc/nginx/server.crt ]]; then
	echo "Sign the certificate using the above private key and CSR..."
	vvvsigncert="$(openssl x509 -req -days 365 -in /etc/nginx/server.csr -signkey /etc/nginx/server.key -out /etc/nginx/server.crt 2>&1)"
	echo $vvvsigncert
fi

cp /vagrant/provision/init/nginx/files/nginx.conf /etc/nginx/nginx.conf
cp /vagrant/provision/init/nginx/files/nginx-wp-common.conf /etc/nginx/nginx-wp-common.conf

if [[ ! -d /etc/nginx/custom-sites ]]; then
	mkdir /etc/nginx/custom-sites/
fi

cp /vagrant/provision/init/nginx/files/main-site.conf /etc/nginx/custom-sites/main-site.conf