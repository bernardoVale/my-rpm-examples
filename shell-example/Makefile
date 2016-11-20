VERSION=0.2
current_dir = $(shell pwd)

all: clean compress build check

clean:
	rm -rf *.tar.gz
	rm -rf *.rpm

compress:
	mv app app-$(VERSION)	
	tar -cvzf app-$(VERSION).tar.gz app-$(VERSION)
	mv app-$(VERSION) app

build:
	docker run -it --rm -v $(current_dir):/app -v $(current_dir)/build.sh:/build.sh gvangool/rpmbuilder:centos7 /build.sh

check:
	docker run -it --rm -v $(current_dir)/app-$(VERSION)-1.noarch.rpm:/app.rpm \
	-v $(current_dir)/check.sh:/check.sh gvangool/rpmbuilder:centos7 /check.sh
