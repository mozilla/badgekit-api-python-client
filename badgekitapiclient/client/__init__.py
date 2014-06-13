__all__ = ['Client']

from types import MethodType
from utils import get_context
import methods

class Client (object):

    def __init__ (self, remote):
        self._remote = remote

    @property
    def _path (self):
        return ''


def bind (method, name):
    def api_method (self, context=None, *args, **kwargs):
        context = get_context(context or kwargs, self)
        return method(self, context, *args, **kwargs)

    bound_method = MethodType(api_method, None, Client)
    setattr(Client, name, bound_method)
    return bound_method


for name, module in methods.__dict__.items():
    if name[0] != '_':
        for name, method in module.__dict__.items():
            if name[0] != '_':
                bind(method, name)
