# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|

  vagrant_version = Vagrant::VERSION.sub(/^v/, '')

  # config.vm.provider :virtualbox do |v|
  #   v.customize ["modifyvm", :id, "--memory", 512]
  # end

  config.vm.box      = "ubuntu14.04i386"
  config.vm.box_url  = "http://cloud-images.ubuntu.com/vagrant/trusty/current/trusty-server-cloudimg-i386-vagrant-disk1.box"
  config.vm.hostname = "monkeyrocket"
  config.vm.network :private_network, ip: "192.168.50.4"  
  config.vm.provision :shell, :path => "boot.sh"

  config.ssh.forward_agent = true
end