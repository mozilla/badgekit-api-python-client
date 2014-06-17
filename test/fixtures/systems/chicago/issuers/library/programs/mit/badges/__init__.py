def get (request, query):
    import scratch

    return {
        'badges': [
            scratch.get(request, query)['badge'],
        ]
    }