from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.core.serializers import serialize
from presentation.models import Tweets
import json, datetime

def index(request):
	tweets = Tweets.objects(text__icontains='#arstem')
	return render(request, 'index.html', {'tweets':tweets})

def tweet_counts(request):
	tweets_cnt = { "#wind" : Tweets.objects(text__icontains='#wind').count(), 
		"#coal":Tweets.objects(text__icontains='#coal').count(),
		"#nuclear":Tweets.objects(text__icontains='#nuclear').count(),
		"#hydro":Tweets.objects(text__icontains='#hydro').count()
		}
	return HttpResponse(json.dumps(tweets_cnt), content_type='application/json')

def tweet_counts_qa(request):
	tweets_cnt = { "#arstemwind" : Tweets.objects(text__icontains='#arstemwind').count(), 
		"#arstemcoal":Tweets.objects(text__icontains='#arstemcoal').count(),
		"#arstemnuclear":Tweets.objects(text__icontains='#arstemnuclear').count(),
		"#arstemhydro":Tweets.objects(text__icontains='#arstemhydro').count()
		}
	return HttpResponse(json.dumps(tweets_cnt), content_type='application/json')

def tweets_by_time(request):
	tweets = [{str(datetime.datetime.fromtimestamp(int(t.timestamp_ms)/1000)) : [t.user['followers_count'], t.user['friends_count'], t.user['statuses_count'],t.user['favourites_count']]} for t in Tweets.objects.all()]#(text__icontains='#arstem')]
	return HttpResponse(json.dumps(tweets), content_type='application/json')
