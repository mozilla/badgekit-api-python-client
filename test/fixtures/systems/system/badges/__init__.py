single_response = {
    'badges': [
        {'slug': 'test-1', 'name': 'Test Badge 1'},
    ]
}

all_response = {
    'badges': [
        {'slug': 'test-1', 'name': 'Test Badge 1'},
        {'slug': 'test-2', 'name': 'Test Badge 2'}
    ]
}

def get (request, query):
    if query.get('archived') == 'any':
        return all_response
    return single_response