#!/bin/sh
# setup.sh - Installs project

# TODO: Check Ubuntu version on Kinba computer
# This is for Ubuntu 16.04
# http://wiki.ros.org/kinetic/Installation/Ubuntu

# Setup your sources.list
echo '==> setup.sh: Setup your sources.list'
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'

# Set up your keys
echo '==> setup.sh: Setup your keys'
sudo apt-key adv --keyserver hkp://ha.pool.sks-keyservers.net:80 --recv-key 421C365BD9FF1F717815A3895523BAEEB01FA116

# Installation
echo '==> setup.sh: Installation'
sudo apt-get -qq update
sudo apt-get -qq upgrade

echo '==> setup.sh:  Desktop-Full Install'
# Desktop-Full Install
sudo apt-get install -y ros-kinetic-desktop-full
# Alternative: Desktop Install
#sudo apt-get install ros-kinetic-desktop
# Alternative: ROS-Base (Bare Bones)
#sudo apt-get install ros-kinetic-ros-base

echo '==> setup.sh: Initalize rosdep'
# Initalize rosdep
sudo rosdep init
rosdep update

# Environment setup
echo '==> setup.sh: Environment setup'
echo "source /opt/ros/kinetic/setup.bash" >> ~/.bashrc
. ~/.bashrc

# Installing rosintall
echo '==> setup.sh: Installing rosintall'
#sudo apt-get install -y 'python-rosinstall'
