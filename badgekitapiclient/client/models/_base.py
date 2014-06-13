from types import MethodType


def _do_action (item, action, path=None, data=None):
    from badgekitapiclient.client.utils import Generator

    if path is None:
        path = item._path

    constructor = type(item)
    constructor_name = constructor.__name__
    constructor_name = constructor_name[0].lower() + constructor_name[1:]

    options = {
        'path': path,
        'filter': constructor_name,
        'generator': Generator(constructor, item._parent),
    }

    if data is not None:
        options['data'] = data

    return getattr(item._remote, action)(options)


class BaseModel (dict):
    def __init__ (self, data, parent):
        if (not isinstance(data, dict)):
            data_property = getattr(type(self), 'path_identifier', 'slug')
            data = {data_property: data}

        super(BaseModel, self).__init__(**data)

        self._parent = parent

    def __get__ (self, key):
        return self._data[key]

    @property
    def _heritage (self):
        heritage = {}
        parent = self._parent

        while (parent):
            key = parent.constructor.name.lower() or 'client'
            heritage[key] = parent
            parent = parent._parent

        return heritage

    @property
    def _remote (self):
        return self._parent._remote

    @property
    def _path (self):
        return self._parent._path + self._get_path_part()

    def create (self):
        path = self._parent._path + type(self).path_part
        return _do_action(self, 'post', path=path, data=dict(self))

    def load (self):
        return _do_action(self, 'get')

    def save (self):
        return _do_action(self, 'put', data=dict(self))

    def delete (self):
        return _do_action(self, 'delete');

    def _get_path_part (self):
        constructor = type(self)
        identifier = getattr(constructor, 'path_identifier', 'slug')
        return '%s/%s' % (constructor.path_part, self.get(identifier))
