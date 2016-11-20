current_dir = $(shell pwd)

all: clean build-deps spec build

build-deps:
	docker build -t py2pack -f Dockerfile_base .

clean:
	rm -rf *.spec
	rm -rf *.tar.gz
	rm -rf *.rpm

spec:
	docker run -it --rm \
	-v $(current_dir)/build_spec.sh:/build_spec.sh \
	-v $(current_dir):/app \
	 py2pack:latest /build_spec.sh

build:
	docker run -it --rm -v $(current_dir):/app -v $(current_dir)/build.sh:/build.sh gvangool/rpmbuilder:centos6 /build.sh 3.1.0
