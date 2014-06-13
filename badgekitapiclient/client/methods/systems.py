from badgekitapiclient import models
from badgekitapiclient.client.utils import context_requires, Generator

def get_systems (client):
    options = {
        'path': client._path + models.System.path_part,
        'filter': 'systems',
        'default': [],
        'generator': Generator(models.System, client),
    }

    return client._remote.get(options)


def get_system (client, context):
    return _do_system_action(client, context, 'load')


def create_system (client, context):
    return _do_system_action(client, context, 'create')


def delete_system (client, context):
    return _do_system_action(client, context, 'delete')


def update_system (context, callback):
    return _do_system_action(client, context, 'save')


@context_requires(models.System)
def _do_system_action (client, context, action):
    return getattr(context, action)()
