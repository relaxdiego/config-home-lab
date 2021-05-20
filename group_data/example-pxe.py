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
        "root_dir": "/opt/home-lab/pxe/tftp"
    }
}
