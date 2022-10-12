FROM python:latest

RUN apt-get update -y && apt-get upgrade -y

VOLUME /code

WORKDIR /code

COPY ./src /code

# Install bump so we can use this for the build
RUN pip install bumpversion

# We're installing the project into the container so later we can mount straight into Python's dist packages and develop live

RUN pip install -r requirements.txt && \
    python setup.py install --single-version-externally-managed --root=/