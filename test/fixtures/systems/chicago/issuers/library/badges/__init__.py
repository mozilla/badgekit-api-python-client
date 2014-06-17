def get (request, query):
    import library

    return {
        'badges': [
            library.get(request, query)['badge'],
        ]
    }