#! /usr/bin/env bash

#sudo apt update
#sudo apt upgrade
sudo apt install -y build-essential \
	autoconf \
	git \
	pkg-config \
	fig2dev \
	bison \
	gnutls-dev \
	libsqlite3-dev \
	libldap-dev \
	zlib1g-dev \
	libreadline-dev \
	thunderbird \
	python2.7

test -e /usr/bin/python2 || sudo ln -s /usr/bin/python2.7 /usr/bin/python2
sudo rm -f /etc/ImageMagick-6/policy.xml

git config --global user.email dc-demo@example.com
git config --global user.name DC Demo
