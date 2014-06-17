data = {
    'slug': 'pittsburgh',
    'name': 'Pittsburgh',
    'url': 'http://pittsburghpa.gov',
    'imageUrl': 'http://example.org/test.png',
    'id': 2,
    'email': 'mayor-ravenstahl@pittsburghpa.gov',
    'issuers': []
}

def get (request, query):
    rsp = data.copy()
    return {'system': rsp}
