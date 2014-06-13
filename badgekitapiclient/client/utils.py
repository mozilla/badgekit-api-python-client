from badgekitapiclient import models
from badgekitapiclient.models._base import BaseModel

class ContextError (Exception):
    pass


def get_context (context, client):
    if type(context) is BaseModel:
        return context

    if 'system' not in context:
        raise ContextError('Missing system')

    current_context = models.System(context['system'], client)

    if 'issuer' in context:
        current_context = models.Issuer(context['issuer'], current_context)

    if 'program' in context:
        if type(current_context) is not models.Issuer:
            raise ContextError('Missing issuer')

        current_context = models.Program(context['program'], current_context)

    if 'badge' in context:
        current_context = models.Badge(context['badge'], current_context)

    return current_context


def context_requires (*required_models):
    def wrapper (method):
        def context_checker (client, context, *args, **kwargs):
            if type(context) not in required_models:
                # TO DO: raise exception here
                pass

            return method(client, context, *args, **kwargs)
        return context_checker
    return wrapper


class Generator (object):
    def __init__ (self, constructor, parent, preformat=None):
        self._constructor = constructor
        self._parent = parent

        if not callable(preformat) \
                and hasattr(constructor, 'parseResponse') \
                and callable(constructor.parseResponse):
            preformat = constructor.parseResponse

        self._preformat = preformat

    def __call__ (self, data):
        if data is None:
            return None

        if type(data) == dict:
            return self._constructor(data, self._parent)

        return [self._constructor(item, self._parent) for item in data]

    def preformat (self, data):
        if callable(self._preformat):
            return self._preformat(data)
        return data
