from badgekitapiclient import models
from badgekitapiclient.client.utils import context_requires, Generator

__all__ = [
    'get_badges',
    'get_all_badges',
    'get_badge',
    'create_badge',
    'delete_badge',
    'update_badge',
]

container_models = (models.System, models.Issuer, models.Program,)

@context_requires(*container_models)
def get_badges (client, context, **kwargs):
    return _find_badges(client, context)


@context_requires(*container_models)
def get_all_badges (client, context, **kwargs):
    return _find_badges(client, context, {'archived': 'any'})


def get_badge (client, context, **kwargs):
    return _do_badge_action(client, context, 'load')


def create_badge (client, context, **kwargs):
    return _do_badge_action(client, context, 'create')


def delete_badge (client, context, **kwargs):
    return _do_badge_action(client, context, 'delete')


def update_badge (context, callback, **kwargs):
    return _do_badge_action(client, context, 'save')


def _find_badges (client, context, query=None):
    options = {
        'path': context._path + models.Badge.path_part,
        'filter': 'badges',
        'default': [],
        'generator': Generator(models.Badge, context),
        'query': query
    }

    return client._remote.get(options)


@context_requires(models.Badge)
def _do_badge_action (client, context, action):
    return getattr(context, action)()
