build-cli-docker-dev-img:
	docker build --rm \
		-t ghcr.io/dlemphers/dbx:cli-dev \
		-f Dockerfile .. 
	docker push ghcr.io/dlemphers/dbx:cli-dev

build-cli-docker-pyinstaller-img:
	docker build --rm \
		-t ghcr.io/dlemphers/dbx:cli-pyinstaller \
		-f Dockerfile.pyinstaller .. 
	docker push ghcr.io/dlemphers/dbx:cli-pyinstaller

		