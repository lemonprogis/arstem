# SPP AR Stem Presentation

Sample Project used in demonstrating what SPP does, using twitter api.

## Installation
below are what's used in this demo

python
https://www.python.org/ 

MongoDB
https://www.mongodb.com

Django
https://www.djangoproject.com/  

MongoEngine
http://mongoengine.org/ 

Pymongo
https://api.mongodb.org/python/current/ 

Tweepy
http://www.tweepy.org/ 


## Usage

You'll need to create a JSON Configuration file named "TweetReader.json" for your Twitter API credentials. This JSON will look like this:

{
	"consumer_key":"",
	"consumer_secret":"",
	"access_token":"",
	"access_token_secret":""
}



Once the above components have been installed, you can run the tweet collector
python collect_tweets.py

run as background process on linux
python collect_tweets.py & 

in another command window/terminal run django web application....

cd /arstem
python manage.py runserver 

navigate to http://localhost:8000/tweets

Happy Coding :)

## Credits

ed briggler
eric wyles

## License
GNU

this is a sample project and used as an instructional tool. no warranties, no worries. 
