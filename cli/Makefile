develop-cli-locally:
	-docker rm -f devbox-http-echo
	-docker run -d \
		--name devbox-http-echo \
		hashicorp/http-echo \
		-text="9x3s8ff"

	docker run --rm \
		-ti \
		-v `pwd`/src/devbox:/usr/local/lib/python3.10/site-packages/devbox \
		-v /etc/hosts:/etc/hosts \
		-v /var/run/docker.sock:/var/run/docker.sock \
		ghcr.io/dlemphers/devbox:cli-dev \
		devbox network docker --update-hosts-file
	
	curl http://devbox-http-echo:5678

	-docker rm -f devbox-http-echo
