def get (request, query):
    return {
        'issuers': [{
            'id': 1,
            'slug': 'test',
            'url': '',
            'name': 'Test Issuer',
            'description': None,
            'email': None,
            'imageUrl': None,
            'programs': []
        }]
    }
