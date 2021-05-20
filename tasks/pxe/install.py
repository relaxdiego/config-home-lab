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

dnsmasq_conf = files.template(
    name='Render the dnsmasq config',
    src='templates/pxe/dnsmasq.conf.j2',
    dest='/etc/dnsmasq.conf',
    mode='744',
    user='root',
    group='root',
    sudo=True,
    dnsmasq=host.data.dnsmasq,
)

systemd.service(
    name='Restart dnsmasq',
    service='dnsmasq',
    running=True,
    restarted=dnsmasq_conf.changed,
    sudo=True,
)
