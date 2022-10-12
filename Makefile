include .maketools/ghcr

login: 
	$(login)

build-cli-docker-dev-img: login

	$(MAKE) -C cli/.docker build-cli-docker-dev-img

build-cli-docker-pyinstaller-img: login

	$(MAKE) -C cli/.docker build-cli-docker-pyinstaller-img

develop-cli-locally:

	$(MAKE) -C cli develop-cli-locally 

test-cli-locally:

	$(MAKE) -C cli test-cli-locally 	

compile-cli-binary:

	$(MAKE) -C cli compile-cli-binary
