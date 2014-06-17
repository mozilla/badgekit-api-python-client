data = {
    'consumerDescription': 'A consumer description of the Chicago Scratch Badge',
    'rubricUrl': 'http://example.org/chicaogScratchRubric',
    'strapline': 'A badge for doing Scratch in Chicago',
    'id': 4,
    'issuer': {
        'slug': 'library',
        'description': 'Chicago Public Library',
        'programs': [],
        'url': 'http://www.chipublib.org/',
        'imageUrl': None,
        'id': 1,
        'email': 'eratosthenes@chipublib.org',
        'name': 'Chicago Public Library'
    },
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
    'issuerUrl': 'http://example.org/chicagoIssuerUrl',
    'program': {
        'slug': 'mit',
        'description': 'Create stories, games, and animations. Share with others around the world',
        'url': 'http://scratch.mit.edu/',
        'imageUrl': None,
        'id': 1,
        'email': 'admin@scratch.mit.edu',
        'name': 'MIT Scratch'
    },
    'criteria': [],
    'type': 'Not too shabby',
    'tags': [],
    'timeUnits': 'hours',
    'unique': 1,
    'slug': 'scratch',
    'categories': [],
    'earnerDescription': 'An earner description of the Chicago Scratch Badge',
    'milestones': [],
    'name': 'Chicago Scratch Badge',
    'created': '2014-06-17T10:27:42.000Z',
    'imageUrl': 'http://example.org/test.png',
    'timeValue': 5,
    'limit': 2,
    'criteriaUrl': 'http://example.org/chicagoScratchCriteria'
}

def get (request, query):
    rsp = data.copy()
    return {'badge': rsp}
