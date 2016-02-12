# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
  config.vm.box = "ubuntu/trusty64"
  config.ssh.insert_key = false
  config.vm.network "private_network", ip: "192.168.60.10"

  config.vm.provider "virtualbox" do |vb|
    vb.memory = "512"
  end
  
  config.vm.provision "ansible" do |ansible|
    ansible.playbook = "askit-playbook.yml"
  end
end
