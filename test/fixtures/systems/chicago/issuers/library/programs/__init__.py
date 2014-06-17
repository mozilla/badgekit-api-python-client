def get (request, query):
    import mit

    return {
        'programs': [
            mit.get(request, query)['program'],
        ]
    }
