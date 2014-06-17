data = {
    'slug': 'library',
    'description': 'Chicago Public Library',
    'programs': [],
    'url': 'http://www.chipublib.org/',
    'imageUrl': 'http://example.org/test.png',
    'id': 1,
    'email': 'eratosthenes@chipublib.org',
    'name': 'Chicago Public Library'
}

def get (request, query):
    import programs

    rsp = data.copy()
    rsp['programs'] = programs.get(request, query)['programs']
    return {'issuer': rsp}
