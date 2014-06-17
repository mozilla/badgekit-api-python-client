from _actionable import ActionableModel

class Badge (ActionableModel):
    def __init__ (self, data, parent):
        client = parent
        while client._parent:
            client = client._parent

        if 'system' in data:
            from system import System
            parent = data['system'] = System(data['system'], client)

        if 'issuer' in data:
            from issuer import Issuer
            parent = data['issuer'] = Issuer(data['issuer'], data['system'])

        if 'program' in data:
            from program import Program
            parent = data['program'] = Program(data['program'], data['issuer'])

        super(Badge, self).__init__(data, parent)


Badge.path_part = '/badges'
