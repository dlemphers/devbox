from .helpers.docker import sync_containers_ips_with_hostsfile

import click

@click.command()
@click.option('--update-hosts-file', default=True, is_flag=True, help='sync container IPs with hostsfile')
def docker(update_hosts_file):
    if update_hosts_file:
        sync_containers_ips_with_hostsfile()

@click.group(
    short_help='Configure local network',
    commands=[
        docker
    ]
)
def network():
    pass

