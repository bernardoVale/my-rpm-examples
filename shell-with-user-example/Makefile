VERSION= $(shell cat VERSION)
current_dir = $(shell pwd)

all: clean compress build check

v:
	@echo "App Version v$(VERSION)"

clean:
	rm -rf *.tar.gz
	rm -rf *.rpm

compress:
	mv app app-$(VERSION)	
	tar -cvzf app-$(VERSION).tar.gz app-$(VERSION)
	mv app-$(VERSION) app

build:
	docker run -it --rm -v $(current_dir):/app -v $(current_dir)/build.sh:/build.sh gvangool/rpmbuilder:centos7 /build.sh $(VERSION)

check:
	docker run -it --rm -v $(current_dir)/app-$(VERSION)-1.noarch.rpm:/app.rpm \
	-v $(current_dir)/check.sh:/check.sh gvangool/rpmbuilder:centos7 /check.sh

test:
		docker build -t test .
		@echo "Execute below docker command to access the container:"
		@echo "docker run -it --rm test"