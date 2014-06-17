data = {
    'consumerDescription': 'A consumer description of the Chicago Library Badge', 
    'rubricUrl': 'http://example.org/chicaogLibraryRubric', 
    'strapline': 'A badge for doing Library in Chicago', 
    'id': 5, 
    'issuer': {
        'slug': 'chicago-library', 
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
    'criteria': [], 
    'type': 'Not too shabby', 
    'tags': [], 
    'timeUnits': 'hours', 
    'unique': 1, 
    'slug': 'chicago-library-badge', 
    'categories': [], 
    'earnerDescription': 'An earner description of the Chicago Library Badge', 
    'milestones': [], 
    'name': 'Chicago Library Badge', 
    'created': '2014-06-17T10:27:42.000Z', 
    'imageUrl': 'http://example.org/test.png', 
    'timeValue': 5, 
    'limit': 2, 
    'criteriaUrl': 'http://example.org/chicagoLibraryCriteria'
}

def get (request, query):
    rsp = data.copy()
    return {'badge': rsp}
