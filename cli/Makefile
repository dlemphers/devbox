start-echo-server:
	-docker rm -f dbx-http-echo
	-docker run -d \
		--name dbx-http-echo \
		hashicorp/http-echo \
		-text="9x3s8ff"

stop-echo-server:
	-docker rm -f dbx-http-echo

test-cli-locally: start-echo-server

	docker run --rm \
		-ti \
		-v `pwd`/src/dbx:/usr/local/lib/python3.10/site-packages/dbx \
		-v /etc/hosts:/etc/hosts \
		-v /var/run/docker.sock:/var/run/docker.sock \
		ghcr.io/dlemphers/dbx:cli-dev \
		dbx network docker --update-hosts-file
	
	curl http://dbx-http-echo:5678

	$(MAKE) stop-echo-server

develop-cli-locally: start-echo-server

	docker run --rm \
		-ti \
		-v `pwd`/src/dbx:/usr/local/lib/python3.10/site-packages/dbx \
		-v /etc/hosts:/etc/hosts \
		-v /var/run/docker.sock:/var/run/docker.sock \
		ghcr.io/dlemphers/dbx:cli-dev \
		bash
	
	$(MAKE) stop-echo-server

compile-cli-binary:
	docker run --rm \
		-t \
		-v `pwd`/src:/src \
		-v `pwd`/.dist:/.dist \
		-w /.dist \
		ghcr.io/dlemphers/dbx:cli-pyinstaller \
		sh build_exe.sh
