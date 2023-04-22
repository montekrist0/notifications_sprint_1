from os import environ

DEBUG = environ.get('DEBUG', False) == 'True'
ALLOWED_HOSTS = []


# ALLOWED_HOSTS = [
#     host.strip() for host in environ.get('ALLOWED_HOSTS').split(',')
# ]
#
# INTERNAL_IPS = [
#     host.strip() for host in environ.get('INTERNAL_IPS').split(',')
# ]
#
# if DEBUG:
#     import socket  # only if you haven't already imported this
#     hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
#     INTERNAL_IPS += \
#         [ip[: ip.rfind(".")] + ".1" for ip in ips] + ["127.0.0.1", "10.0.2.2"]