from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'presentation.views.index'),
    url(r'^counts/$', 'presentation.views.tweet_counts'),
    url(r'^qa-counts/$', 'presentation.views.tweet_counts_qa'),
    url(r'^time-series/$', 'presentation.views.tweets_by_time'),
)