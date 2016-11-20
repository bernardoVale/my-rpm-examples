#!/usr/bin/env bash
VERSION=0.2

cp /app/app-${VERSION}.tar.gz /root/rpmbuild/SOURCES

rpmbuild --ba /app/simple-app.spec

cp /root/rpmbuild/RPMS/noarch/app-${VERSION}-1.noarch.rpm /app