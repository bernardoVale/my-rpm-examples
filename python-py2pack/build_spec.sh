#!/bin/bash
py2pack fetch terminaltables
py2pack generate terminaltables -t opensuse.spec -f /app/terminaltables.spec
cp /terminaltables-3.1.0.tar.gz /app