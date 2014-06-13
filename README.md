# Python BadgeKit API Client

A client for the BadgeKit API, in Python

## Usage

```python
from badgekitapiclient import init

endpoint = 'http://api.example.org'
auth = {'key': 'auth key', 'secret': 'auth secret'}
client = init(endpoint, auth)

badges = client.get_badges(system='system-slug')
for badge in badges:
    print badge['name']
```

## Testing

```
python test
```