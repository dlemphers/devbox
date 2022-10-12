import click

from dbx.extensions.network import network

VERSION = "0.0.8"

@click.group(
    commands=[network.network]
)
def main():
    pass

if __name__ == "__main__":
    main()