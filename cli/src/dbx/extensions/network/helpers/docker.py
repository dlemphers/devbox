import sys
import shutil

import click
import jmespath

import docker as Docker

docker_daemon = Docker.from_env()

def sync_containers_ips_with_hostsfile(filter):
    click.echo("Filtering on: {}".format(filter))

    containers = docker_daemon.containers.list()
    container_mapping = {}

    for container in containers:
        container_ip_address = jmespath.search(
            'NetworkSettings.Networks | values(@)[0] | IPAddress',
            container.attrs
        )

        container_name = jmespath.search(
            'Name',
            container.attrs
        ).replace('/','')

        if container_ip_address:
            container_mapping[container_ip_address] = container_name

    update_hosts_file(container_mapping, filter)

def update_hosts_file(container_mappings, hostname_filter):

    click.echo("Updating /etc/host with Docker container IP addresses")

    host_file = '/etc/hosts'

    try:
        shutil.copy2(host_file, '/tmp/hosts_backup')
        
        hosts_lines = list(
            filter(
                None, 
                open(host_file).readlines()
            )
        )

        if len(hosts_lines) == 0:
            hosts_lines.append('')

        for i, _ in enumerate(hosts_lines, 0):
            if '#dbx' in hosts_lines[i]:
                # This is a dbx managed line
                # Check if container still exists
                ip_address, hostname, _ = hosts_lines[i].split(" ")
                if hostname not in container_mappings.values():
                    # This doesn't exist in docker anymore so remove it
                    hosts_lines[i] = ''

        new_entries = []

        for container_ip_address, container_name in container_mappings.items():

            if hostname_filter and hostname_filter not in container_name:
                continue

            entry_location = None
            entry_line = '{} {} #dbx\n'.format(
                container_ip_address, container_name
            )

            for i, _ in enumerate(hosts_lines, 0):
                if container_ip_address in hosts_lines[i] or container_name in hosts_lines[i]:
                    entry_location = i

                    hosts_lines[i] = entry_line

            if not entry_location:
                new_entries.append(entry_line)

        new_hosts_file = list(set(hosts_lines)) + list(set(new_entries))

        open(host_file, 'w').write(''.join(new_hosts_file))
    except Exception as ex:
        click.echo("Error: {}".format(ex))
        click.ClickException(ex)
        shutil.copy2('/tmp/hosts_backup', host_file)        
