#!/usr/bin/env bash
VERSION="$1"

yum install -y python-devel python-setuptools

cp /app/terminaltables-${VERSION}.tar.gz /root/rpmbuild/SOURCES

rpmbuild --ba /app/terminaltables.spec

cp /root/rpmbuild/RPMS/noarch/python-terminaltables-${VERSION}-0.noarch.rpm /app