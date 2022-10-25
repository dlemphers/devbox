from .helpers.docker import sync_containers_ips_with_hostsfile

import click

@click.command()
@click.option(
    '--update-hosts-file', 
    default=True, 
    is_flag=True, 
    help='sync container IPs with hostsfile')
@click.option(
    '--filter', 
    default='', 
    is_flag=False, 
    help='filter hostname entries')

def docker(update_hosts_file, filter):
    if update_hosts_file:
        sync_containers_ips_with_hostsfile(filter)

@click.group(
    short_help='Configure local network',
    commands=[
        docker
    ]
)
def network():
    pass

