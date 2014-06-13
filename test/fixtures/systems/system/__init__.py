import issuers

def get (request, query):
    return {
        'system': {
            'id': 1,
            'slug': 'system',
            'url': '',
            'name': 'Test System',
            'email': None,
            'imageUrl': None,
            'issuers': issuers.get(request, query)['issuers']
        }
    }
