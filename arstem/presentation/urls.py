from django.conf.urls import url
from presentation.views import tweet_counts, tweet_counts_qa, tweets_by_time, index

urlpatterns = [
    url(r'^$', index),
    url(r'^counts/$', tweet_counts),
    url(r'^qa-counts/$', tweet_counts_qa),
    url(r'^time-series/$', tweets_by_time)
]