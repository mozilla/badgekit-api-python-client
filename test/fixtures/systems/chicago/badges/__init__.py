def get (request, query):
    import badge
    import archived
    from ..issuers.library.badges import library
    from ..issuers.library.programs.mit.badges import scratch

    badges = [
        badge.get(request, query)['badge'],
        archived.get(request, query)['badge'],
        library.get(request, query)['badge'],
        scratch.get(request, query)['badge'],
    ]

    if query.get('archived') != 'any':
        badges = [badge for badge in badges if not badge['archived']]

    return {'badges': badges}

def post (request, query):
    badge = request['data']
    errors = validateBadge(badge)
    if len(errors):
        return ({
            'message': 'Could not validate required fields', 
            'code': 'ValidationError', 
            'details': [{'field': field, 'value': ''} for field in errors]
        }, 400)

    return {
        'status': 'created',
        'badge': {
            'id': 99,
            'slug': badge.get('slug'),
            'name': badge.get('name'),
            'strapline': badge.get('strapline'),
            'earnerDescription': badge.get('earnerDescription'),
            'consumerDescription': badge.get('consumerDescription'),
            'issuerUrl': badge.get('issuerUrl'),
            'rubricUrl': badge.get('rubricUrl'),
            'timeValue': badge.get('timeValue'),
            'timeUnits': badge.get('timeUnits'),
            'limit': badge.get('limit'),
            'unique': badge.get('unique'),
            'created': '2014-06-17T13:14:33.000Z',
            'imageUrl': badge.get('imageUrl'),
            'type': badge.get('type'),
            'archived': False,
            'system': {
                'id': 1,
                'slug': 'chicago',
                'url': 'http://cityofchicago.org',
                'name': 'Chicago',
                'email': 'mayor-emanuel@cityofchicago.org',
                'imageUrl': None,
                'issuers': []
            },
            'criteriaUrl': badge.get('criteriaUrl'),
            'criteria': [],
            'categories': [],
            'tags': [],
            'milestones': []
        }
    }


def validateBadge (badge):
    missing = []
    for field in required_fields:
        if field not in badge:
            missing.append(field)
    return missing

required_fields = ('name', 'slug', 'earnerDescription', 'consumerDescription',
                        'criteriaUrl', 'unique', 'image', 'type',)

