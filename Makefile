include .maketools/ghcr

login: 
	$(login)

build-cli-docker-dev-img: login

	$(MAKE) -C cli/.docker build-cli-docker-dev-img
	
develop-cli-locally:

	$(MAKE) -C cli develop-cli-locally 