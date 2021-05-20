# These are the machines that will be part of the PXE service
# that will configure the baremetals and KVM machines in my lab
#
# The hostnames may be resolved by a DNS server in the network
# or they could just be hosts declared in your ~/.ssh/config file.
# For example:
#
# Host homelab-pxe-server
#     HostName <IP-ADDRESS-HERE>
#     User <USERNAME-HERE>
#
# If other ssh config options apply, add them as needed.

pxe_server = [
    'homelab-pxe-server'
]
