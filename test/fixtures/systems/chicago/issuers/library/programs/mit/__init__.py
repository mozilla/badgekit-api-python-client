data = {
    'slug': 'mit', 
    'description': 'Create stories, games, and animations. Share with others around the world', 
    'url': 'http://scratch.mit.edu/', 
    'imageUrl': 'http://example.org/test.png', 
    'id': 1, 
    'email': 'admin@scratch.mit.edu', 
    'name': 'MIT Scratch'
}

def get (request, query):
    rsp = data.copy()
    return {'program': rsp}
