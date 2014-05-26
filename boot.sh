apt-get update
apt-get install dos2unix
wget https://raw.githubusercontent.com/pypa/pip/master/contrib/get-pip.py
python get-pip.py
rm get-pip.py
apt-get clean
pip install docopt

find /vagrant/cli -exec dos2unix '{}' \;

# cp -r /vagrant/cli /home/monkey_cli
# cd /home/monkey_cli
# python setup.py sdist
# cd dist
# tar -xvzf monkey-1.0.tar.gz
# cd monkey-1.0
# python setup.py install
# cp /vagrant/cli/monkey /usr/local/bin