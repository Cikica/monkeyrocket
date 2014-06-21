provision_folder="/vagrant/provision/init"

start_time="$(date +%s)"

apt_package_install_list=()
module_list=(
	tools
	php
	nginx
	memcached
	mysql
	wordpress
)
apt_package_check_list=()

for package in "${module_list[@]}"; do
	echo " - running $provision_folder/$package/packages.sh"
	source "$provision_folder/$package/packages.sh"
	apt_package_check_list=("${apt_package_check_list[@]}" "${packages[@]}" )
done

for package in "${apt_package_check_list[@]}"; do

	package_version="$(dpkg -s $package 2>&1 | grep 'Version:' | cut -d " " -f 2)"
	if [[ -n "${package_version}" ]]; then
		space_count="$(expr 20 - "${#package}")"
		pack_space_count="$(expr 30 - "${#package_version}")"
		real_space="$(expr ${space_count} + ${pack_space_count} + ${#package_version})"
		printf " * $package %${real_space}.${#package_version}s ${package_version}\n"
	else
		echo " *" $package [not installed]
		apt_package_install_list+=($package)
	fi
done

for package in "${module_list[@]}"; do 
	if [[ -a "$provision_folder/$package/pre.sh" ]]; then
		echo " - pre configuration for $package"
		source "$provision_folder/$package/pre.sh"
	fi
done

apt-get update
apt-get install --assume-yes ${apt_package_install_list[@]}
apt-get clean

cp /vagrant/provision/mb-init.conf /etc/init/mb-init.conf

for package in "${module_list[@]}"; do 
	if [[ -a "$provision_folder/$package/boot1.sh" ]]; then
		echo " - boot1 configuration for $package"
		source "$provision_folder/$package/boot1.sh"
	fi
done

for package in "${module_list[@]}"; do 
	if [[ -a "$provision_folder/$package/boot2.sh" ]]; then
		echo " - boot2 configuration for $package"
		source "$provision_folder/$package/boot2.sh"
	fi
done

end_time="$(date +%s)"
minutes_taken=$(( ( $end_time - $start_time )/60))
seconds_taken=$(( ( $end_time - $start_time ) - $minutes_taken*60 ))
echo " # provision took $minutes_taken:$seconds_taken"
# phpdis something seems to not be recognised