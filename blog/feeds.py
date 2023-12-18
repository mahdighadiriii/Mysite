from django.contrib.syndication.views import Feed
from django.urls import reverse
from blog.models import Post

class LatestEntriesFeed(Feed):
    title = "Blog news"
    link = "/rss/feed"
    description = "All the post in my site"

    def items(self):
        return Post.objects.filter(status=True)

    def item_title(self, item):
        return item.title

    def item_decription(self, item):
        return item.content[:255]