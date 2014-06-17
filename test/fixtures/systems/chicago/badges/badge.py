data = {
    'consumerDescription': 'A consumer description of the Chicago Badge',
    'rubricUrl': 'http://example.org/chicagoRubric',
    'strapline': 'A badge for Chicago',
    'id': 1,
    'archived': False,
    'system': {
        'slug': 'chicago',
        'name': 'Chicago',
        'url': 'http://cityofchicago.org',
        'imageUrl': None,
        'id': 1,
        'email': 'mayor-emanuel@cityofchicago.org',
        'issuers': []
    },
    'issuerUrl': 'http://example.org/chicagoIssuer',
    'criteria': [
        {
            'note': 'Some sort of note',
            'required': 1,
            'id': 1,
            'description': 'Just your basic criterion.'
        }
    ],
    'type': 'Not too shabby',
    'tags': [],
    'timeUnits': 'minutes',
    'unique': 1,
    'slug': 'badge',
    'categories': [],
    'earnerDescription': 'An earner description of the Chicago Badge',
    'milestones': [],
    'name': 'Chicago Badge',
    'created': '2014-06-17T10:27:42.000Z',
    'imageUrl': 'http://example.org/test.png',
    'timeValue': 10,
    'limit': 5,
    'criteriaUrl': 'http://example.org/chicagoCriteria'
}

def get (request, query):
    return {'badge': data.copy()}

def put (request, query):
    badge = data.copy()
    for key, value in request['data'].items():
        badge[key] = value

    return {
        'status': 'updated',
        'badge': badge,
    }

def delete (request, query):
    if 'deleted' in data:
        raise ImportError('Deleted!')

    badge = data.copy()
    data['deleted'] = True

    return {
        'status': 'deleted',
        'badge': badge,
    }
