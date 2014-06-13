__version__ = 1.0

from client import Client
from remote import Remote

def init (endpoint, auth):
    remote = Remote(endpoint, auth)
    client = Client(remote)

    return client
