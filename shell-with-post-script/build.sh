#!/usr/bin/env bash
VERSION="$1"

cp /app/app-${VERSION}.tar.gz /root/rpmbuild/SOURCES

rpmbuild --ba --define "_app_version $VERSION" /app/simple-app.spec

cp /root/rpmbuild/RPMS/noarch/app-${VERSION}-1.noarch.rpm /app