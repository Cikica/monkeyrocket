apt-get update
apt-get install dos2unix
wget https://raw.githubusercontent.com/pypa/pip/master/contrib/get-pip.py
python get-pip.py
rm get-pip.py
apt-get clean
pip install docopt
find /vagrant/cli -exec dos2unix '{}' \;

cp -r /vagrant/cli ~/cli