VERSION= $(shell cat VERSION)
current_dir = $(shell pwd)

all: clean compress build check

version:
	@echo "App Version v$(VERSION)"

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

test:
		docker run -d --name rpm_test centos /sbin/init
		docker cp app-$(VERSION)-1.noarch.rpm rpm_test:/
		docker exec rpm_test bash
		docker stop rpm_test && docker rm rpm_test