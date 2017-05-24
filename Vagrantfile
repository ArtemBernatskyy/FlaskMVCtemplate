Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/trusty64"
  config.vm.synced_folder ".", "/var/webapps/transfer_sys/code",
    owner: "transfer_user", group: "users"
  config.ssh.insert_key=false
  config.vm.box_check_update = false
  config.vm.network :forwarded_port, guest: 22, host: 2339, id: "ssh"
  config.vm.network "forwarded_port", guest: 27017, host: 27017
  config.vm.network :private_network, ip: "172.16.0.73"
  config.vm.provider "virtualbox" do |v|
    v.memory = 512
    v.cpus = 1
    v.name = "TransferSystem"
  end
end