from badgekitapiclient import models
from badgekitapiclient.client.utils import context_requires, Generator

@context_requires(models.System)
def get_issuers (client, context, **kwargs):
    options = {
        'path': context._path + models.Issuer.path_part,
        'filter': 'issuers',
        'default': [],
        'generator': Generator(models.Issuer, context),
    }

    return client._remote.get(options)


def get_issuer (client, context, **kwargs):
    return _do_issuer_action(client, context, 'load')


def create_issuer (client, context, **kwargs):
    return _do_issuer_action(client, context, 'create')


def delete_issuer (client, context, **kwargs):
    return _do_issuer_action(client, context, 'delete')


def update_issuer (context, callback, **kwargs):
    return _do_issuer_action(client, context, 'save')


@context_requires(models.Issuer)
def _do_issuer_action (client, context, action):
    return getattr(context, action)()
