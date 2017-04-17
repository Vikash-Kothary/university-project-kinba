#!/usr/bin/bash
# install-ansible.sh - 
# https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-ansible-on-ubuntu-14-04
# http://ansible.pickle.io/post/86598332429/running-ansible-playbook-in-localhost

sudo apt-get -qq update
sudo apt-get install software-properties-common
sudo apt-get-repository ppa:ansible/ansible
sudo apt-get -qq update
sudo apt-get install ansible