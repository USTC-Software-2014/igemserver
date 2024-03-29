FROM ubuntu:trusty

RUN apt-get update

# install mongodb
RUN apt-get install -y mongodb

# install nginx
RUN apt-get install -y nginx

# install openLDAP
RUN apt-get install slapd libldap2-dev libsasl2-dev libssl-dev

# install python
RUN apt-get install -y python python-dev python-pip build-essential
