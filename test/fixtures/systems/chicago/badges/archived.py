def get (request, query):
    return {
        'badge': {
            'consumerDescription': 'A consumer description of the Archived Badge',
            'rubricUrl': 'http://example.org/archivedRubric',
            'strapline': 'An archived badge',
            'id': 2,
            'archived': True,
            'system': {
                'slug': 'chicago',
                'name': 'Chicago',
                'url': 'http://cityofchicago.org',
                'imageUrl': None,
                'id': 1,
                'email': 'mayor-emanuel@cityofchicago.org',
                'issuers': []
            },
            'issuerUrl': 'http://example.org/archivedIssuer',
            'criteria': [],
            'type': 'Not too shabby',
            'tags': [],
            'timeUnits': 'hours',
            'unique': 1,
            'slug': 'archived',
            'categories': [],
            'earnerDescription': 'An earner description of the Archived Badge',
            'milestones': [],
            'name': 'Archived Badge',
            'created': '2014-06-17T10:27:42.000Z',
            'imageUrl': 'http://example.org/test.png',
            'timeValue': 5,
            'limit': 2,
            'criteriaUrl': 'http://example.org/archivedCriteria'
        }
    }
