import system

def get (request, query):
    return {
        'systems': [
            system.get(request, query)['system']
        ]
    }