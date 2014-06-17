def get (request, query):
    import chicago
    import pittsburgh

    return {
        'systems': [
            chicago.get(request, query)['system'],
            pittsburgh.get(request, query)['system'],
        ]
    }