from badgekitapiclient import init
from badgekitapiclient.remote import RemoteError
import json


client = init('http://localhost:8080', 'something')
programs = client.get_programs(system='test', issuer='test')
for program in programs:
    print program

badges = client.get_badges(system='test')
for badge in badges:
    print badge['name']
# print client.get_all_badges()

# badge = client.get_badge(system='test', badge='test')
# print dir(badge)
# print badge
# print json.dumps(badge)

# 
# badge = {
#     'slug': 'test',
#     'name': 'Test Badge',
#     'earnerDescription': 'Earner Description',
#     'consumerDescription': 'Consumer Description',
#     'criteriaUrl': 'http://example.org/criteria',
#     'unique': True,
#     'image': 'http://example.org/image.png',
#     'type': 'No idea',
# }
# 
# try:
#     print client.create_badge(system='test', badge=badge)
# except RemoteError as err:
#     print type(err), err, err.code