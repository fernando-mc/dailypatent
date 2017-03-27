#!/usr/bin/env python

from ConfigParser import SafeConfigParser
import random
from twython import Twython

r=random

parser = SafeConfigParser()
parser.read('config.ini')

APP_KEY=parser.get('daily_patent','APP_KEY')
APP_SECRET=parser.get('daily_patent','APP_SECRET')
OAUTH_TOKEN=parser.get('daily_patent','OAUTH_TOKEN')
OAUTH_TOKEN_SECRET=parser.get('daily_patent','OAUTH_TOKEN_SECRET')

twitter = Twython(APP_KEY, APP_SECRET,
                  OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

patent_areas = "Utility", "Design"

def tweet(tweet_to_send):
	twitter.update_status(status=tweet_to_send)

def rand_pat_area():
	area = patent_areas[(r.randrange(2))]
	print area
	return area

def url_generators(an_area):
	if an_area == patent_areas[0]:
		final_url = "https://www.google.com/patents/US"+ str(r.randrange(9247000))
		return final_url
		print final_url
	elif an_area == patent_areas[1]:
		final_url = "https://www.google.com/patents/USD"+ str(r.randrange(748365))
		return final_url
		print final_url
	else:
		print "Somehow you broke me!"

def handler(event, context):
	patent_url=url_generators(rand_pat_area())
	prefix_texts=["Here's a #patent you've probably never heard of: ","Will this #random #patent be a troll or the real-deal? ", "I like random #patents. What about you? ","Hey, there's a new random patent: ","How many #patent tweets does it take for you to find something you've used? ","Patents. Patents. #patents. Yup, here's another: "]
	random_prefix=prefix_texts[r.randrange(len(prefix_texts)-1)]
	random_status_update=random_prefix + patent_url
	tweet(random_status_update)
