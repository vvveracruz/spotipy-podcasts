from secret import client_id, client_secret, redirect_uri
import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=client_id,
        client_secret=client_secret,
        redirect_uri=redirect_uri
    )
)

class Episode(object):
    def __init__(self, raw):
        self._raw = raw
        for key in self._raw:
            setattr(self, key, self._raw[key])

class Show(object):
    def __init__(self, uri):
        self._raw = sp.show(uri)
        for key in self._raw:
            setattr(self, '_'+key, self._raw[key])

        self.episodes=[Episode(raw) for raw in self._episodes['items']]
        self.num_episodes = self._episodes['total']

        if self.is_serial:
            # fetch all episodes, to play them in order of release date
            # reorder by order of release date
            pass
    
    @property
    def uri(self):
        return self._uri

    @property
    def is_serial(self):
        '''
        Being a 'serial' show means the episodes will be played in order of
        release date instead of newest first (default).
        ''' 
        if self._is_serial is None:
            # TODO: determine whether a show is serial by checking the file or
            # asking for input 
            self._is_serial = False
        return False


test_show_uri = "6e4HNBdPvjDOHKVf82oMEk"
test_show = Show(test_show_uri)
print(len(test_show.episodes))
print(test_show.num_episodes)

# print(test_show.data.__dict__.keys())
# ep = test_show.episodes[0]
# print(ep.__dict__.keys())
# print(test_show.uri, '\n')
# for n in [0, 1]:
#     print(test_show.episodes['items'][n].keys())
#     print(test_show.episodes['items'][n], '\n')
