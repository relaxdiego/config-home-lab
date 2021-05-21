from pathlib import Path
from pyinfra import (
    host,
)
from pyinfra.operations import (
    apt,
    files,
    systemd,
)


apt.update(
    name="Update apt cache",
    cache_time=30 * 24 * 60 * 60,
    touch_periodic=True,  # touch /var/lib/apt/periodic/update-success-stamp
    sudo=True,
)

apt.packages(
    name='Install dnsmasq',
    packages=['dnsmasq'],
    sudo=True,
)

files.directory(
    name=f'Ensure TFTP root dir {host.data.dnsmasq["tftp"]["root_dir"]}',
    path=host.data.dnsmasq["tftp"]["root_dir"],
    present=True,
    recursive=True,
    sudo=True,
)

for bootloader in host.data.dnsmasq["tftp"]["bootloaders"]:
    bootloader_dir = \
        Path(host.data.dnsmasq["tftp"]["root_dir"]) / bootloader["client_type"]

    files.directory(
        name=f'Ensure bootloader directory {bootloader_dir}',
        path=str(bootloader_dir),
        present=True,
        sudo=True,
    )

    files.download(
        name=f'Download bootloader {bootloader["source_url"]}',
        src=str(bootloader["source_url"]),
        dest=str(bootloader_dir / bootloader["source_url"].split('/')[-1]),
        sha256sum=bootloader["sha256sum"],
        sudo=True,
    )

dnsmasq_conf = files.template(
    name='Render the dnsmasq config',
    src='templates/pxe/dnsmasq.conf.j2',
    dest='/etc/dnsmasq.conf',
    mode='744',
    user='root',
    group='root',
    sudo=True,
    dnsmasq=host.data.dnsmasq,
    machines=host.data.machines,
)

systemd.service(
    name='Restart dnsmasq',
    service='dnsmasq',
    running=True,
    restarted=dnsmasq_conf.changed,
    sudo=True,
)
