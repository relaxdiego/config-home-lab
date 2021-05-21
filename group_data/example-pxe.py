# Copy this file via: cp group_data/example-pxe.py group_data/pxe.py
# then run pyinfra inventory/pxe.py tasks/pxe/install.py
from ipaddress import ip_network


dnsmasq = {
    "interfaces": [
        'eth0',
    ],

    "dhcp": {
        "ranges": [
            {
                "start": "192.168.100.100",
                "end": "192.168.100.250",
            }
        ],
        "subnet": ip_network("192.168.100.0/24"),
        "gateway": "192.168.100.1",
        "dns": [
            "1.1.1.1",
            "8.8.8.8",
        ]
    },

    "tftp": {
        "ip_address": "192.168.100.2",
        "root_dir": "/opt/home-lab/pxe/tftp",

        "bootloaders": [
            {
                "client_type": "kvm-host",
                "source_url": "http://archive.ubuntu.com/ubuntu/dists/focal/main/uefi/grub2-amd64/2.04-1ubuntu26/grubnetx64.efi.signed",  # NOQA
                "sha256sum": "279a5a755bc248d22799434a261b92698740ab817d8aeccbd0cb7409959a1463",  # NOQA
            }
        ],

    },
}

machines = [
    {
        "hostname": "kvm-1",
        "client_type": "kvm-host",
        "mac_address": "f4:4d:30:63:1c:41",
    },
    {
        "hostname": "kvm-2",
        "client_type": "kvm-host",
        "mac_address": "f4:4d:30:63:56:21",
    },
]
