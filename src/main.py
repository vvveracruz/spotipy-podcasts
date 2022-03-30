from secrets import user, password
from pycketcasts import PocketCast

api=PocketCast(user, password)
print(api.subscriptions[0].__dict__)
# print(api.subscriptions)
# for i in api.subscriptions:
#     print(i.title, i._data.get('uuid'))
# print(api.history)
# for i in api.history:
#     print(i.title)
# for i in api.featured:
#     print(i.title)
