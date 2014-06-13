from badgekitapiclient import models
from badgekitapiclient.client.utils import context_requires, Generator

@context_requires(models.Issuer)
def get_programs (client, context, **kwargs):
    options = {
        'path': context._path + models.Program.path_part,
        'filter': 'programs',
        'default': [],
        'generator': Generator(models.Program, context),
    }

    return client._remote.get(options)


def get_program (client, context, **kwargs):
    return _do_program_action(client, context, 'load')


def create_program (client, context, **kwargs):
    return _do_program_action(client, context, 'create')


def delete_program (client, context, **kwargs):
    return _do_program_action(client, context, 'delete')


def update_program (context, callback, **kwargs):
    return _do_program_action(client, context, 'save')


@context_requires(models.Program)
def _do_program_action (client, context, action):
    return getattr(context, action)()
