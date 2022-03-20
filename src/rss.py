import feedparser
import json
import dateparser as dp


class Podcast:
    def __init__(self, url):
        self.url = url
        d = feedparser.parse(url)
        self.feed = d.feed
        self.entries = d.entries
        # podcast_dict = feedparser.parse(url)
        # print(f"Title: {podcast_dict.feed.title}")
        return None


class Episode:
    def __init__(self, pod):
        self.parent = pod
        return None


pod = Podcast("https://feeds.megaphone.fm/badwomen")
ep = Episode(pod)
# print(json.dumps(ep.parent.entries[0], indent=4))
episodes = {i + 1: {} for i in range(len(ep.parent.entries))}
print(episodes)
# for e in ep.parent.entries:
#     print(e.title)
#     print(dp.parse(e.published).strftime("%Y-%m-%d"))
#     print(e.enclosures)
