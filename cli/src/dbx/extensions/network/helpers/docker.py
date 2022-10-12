import sys
import shutil

import click
import jmespath

import docker as Docker

docker_daemon = Docker.from_env()

def sync_containers_ips_with_hostsfile():
    click.echo("Updating /etc/host with Docker container IP addresses")

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

    update_hosts_file(container_mapping)

def update_hosts_file(container_mappings):

    host_file = '/etc/hosts'

    shutil.copy2(host_file, '/tmp/hosts_backup')

    try:
    
        hosts_lines = list(filter(None, open(host_file).readlines()))

        if len(hosts_lines) == 0:
            hosts_lines.append('')

        new_entries = []

        for container_ip_address, container_name in container_mappings.items():

            entry_location = None
            entry_line = '{} {}\n'.format(
                container_ip_address, container_name
            )

            for i, _ in enumerate(hosts_lines, 0):
                if container_ip_address in hosts_lines[i] or container_name in hosts_lines[i]:
                    entry_location = i
                    hosts_lines[i] = entry_line

            if not entry_location:
                new_entries.append(entry_line)

        new_hosts_file = hosts_lines + new_entries

        open(host_file, 'w').write(''.join(new_hosts_file))
    except Exception as ex:
        click.ClickException(ex)
        shutil.copy2('/tmp/hosts_backup', host_file)        
