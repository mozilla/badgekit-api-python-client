from badgekitapiclient import models
from badgekitapiclient.models._base import BaseModel

class ContextError (Exception):
    def __init__ (self, required, received=None):
        if issubclass(required, BaseModel):
            required = (required,)

        if received is not None:
            received = received.__name__

        if len(required) == 1:
            msg = 'Expecting type `%s`' % required[0].__name__
        else:
            msg = 'Expecting one of %s' % [model.__name__ for model in required]

        Exception.__init__(self, '%s: received `%s`' % (msg, received))
        self.required = required
        self.received = received


def get_context (context, client):
    if type(context) is BaseModel:
        return context

    if 'system' not in context:
        raise ContextError(models.System)

    current_context = models.System(context['system'], client)
    del context['system']

    if 'issuer' in context:
        current_context = models.Issuer(context['issuer'], current_context)
        del context['issuer']

    if 'program' in context:
        if type(current_context) is not models.Issuer:
            raise ContextError(models.Issuer)

        current_context = models.Program(context['program'], current_context)
        del context['program']

    if 'badge' in context:
        current_context = models.Badge(context['badge'], current_context)
        del context['badge']

    return current_context


def context_requires (*required_models):
    def wrapper (method):
        def context_checker (client, context, *args, **kwargs):
            context_type = type(context)
            if context_type not in required_models:
                raise ContextError(required_models, context_type)

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
