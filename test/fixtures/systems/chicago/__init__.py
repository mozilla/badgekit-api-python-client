data = {
    'slug': 'chicago',
    'name': 'Chicago',
    'url': 'http://cityofchicago.org',
    'imageUrl': 'http://example.org/test.png',
    'id': 1,
    'email': 'mayor-emanuel@cityofchicago.org',
    'issuers': [],
}

def get (request, query):
    import issuers

    rsp = data.copy()
    rsp['issuers'] = issuers.get(request, query)['issuers']
    return {'system': rsp}
