import click

from devbox.extensions.network import network


@click.group(
    commands=[network.network]
)
def main():
    pass

if __name__ == "__main__":
    main()