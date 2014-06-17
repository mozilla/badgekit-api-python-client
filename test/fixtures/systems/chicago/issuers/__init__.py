def get (request, query):
    import library

    return {
        'issuers': [
            library.get(request, query)['issuer'],
        ]
    }
