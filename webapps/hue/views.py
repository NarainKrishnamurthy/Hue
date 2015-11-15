from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction
from django.http import HttpResponse
from django.http import JsonResponse
from mimetypes import guess_type
from django.core import serializers

# Decorator to use built-in authentication system
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail

# Used to create and manually log in a user
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
import json
import sys, os ,inspect
from hue.models import *
cmd_subfolder  = os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile(inspect.currentframe() ))[0],"Twitter")))

if cmd_subfolder not in sys.path:
     sys.path.insert(0, cmd_subfolder)

import twitter

@transaction.atomic
def home(request):
	context = {}
	context['query'] = False
	context['search_query'] = ''

	if request.method == 'GET':
		return render(request, 'hue/home.html', context)

	if 'search_q' in request.POST:
		search_query = request.POST['search_q']
		context['search_query'] = search_query
        print(search_query)
        context['query'] = True

     #   twitter.twitter_query(search_query)
     #   path = os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile(inspect.currentframe() ))[0],"datumbox")))
     #   file_p = path + '/TextClassification.jar'
     #   ifile  = cmd_subfolder + '/data.json'
     #   ofile  = path + '/sentiment.csv'
     #   os.system("java -jar "+ file_p + ' ' + ifile + ' ' + ofile)
     #   path = os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile(inspect.currentframe() ))[0],"semantic-similarity-master")))
     #   cofile = path + '/senti.json'
     #   os.system(path + "/similar" + ' ' + ifile + ' ' + ofile + ' ' + cofile)
     #   with open(cofile) as data_file:
     #       data = json.load(data_file)
     #   context['data'] = data
     #   print data
     	context['data'] = {u'comm_pos': [{u'text': u"RT @ManUtd: David Beckham's #MatchForChildren kicks off at 15:00 GMT. Get a reminder of the squads: https://t.co/5T4FQJWv0j https://t.co/XT\u2026", u'score': 60776},
     	 {u'text': u'RT @ManUtd: Check out the best #MatchForChildren images in our gallery: https://t.co/l5nJwm6Xti https://t.co/Lz6mjcG2x9', u'score': 29975}, {u'text': u'RT @ManUtd: FT: GB &amp; Ireland 3 Rest of the World 1. Scholes and Owen (2) seal the win, with Yorke on target for ROW. Great game! https://t.\u2026', u'score': 3208}, {u'text': u'RT @IamMSilvestre: 75.000 Prayers at Old Trafford to support my native France  . THANK YOU #ManUtd #PrayForParis \U0001f64f\U0001f3fb\U0001f1eb\U0001f1f7 https://t.co/WyCHSofJ\u2026', u'score': 3046}, 
     	 {u'text': u"RT @ManUtd: From the mohawk to the cornrows, check out Becks' iconic hairstyles ahead of his OT return: https://t.co/tMqDXpSYrZ https://t.c\u2026", u'score': 1766}], u'comm_neg': [{u'text': u'RT @ManUtd: Watch our video to see David Beckham introduce his #MatchForChildren team-mates: https://t.co/hruw8OkTIH https://t.co/LhYv7GNpaV', u'score': 17088}, {u'text': u"RT @ManUtd: Everybody's thoughts at Manchester United are with those who have been affected by Friday's attacks in Paris. https://t.co/RhZE\u2026", u'score': 7213}, {u'text': u'RT @ManUtd: "It\'s embedded in you from day one to take nothing for granted." More from Axel Tuanzebe: https://t.co/OfAbn7d3Sz https://t.co/\u2026', u'score': 410}, {u'text': u"RT @ManUtd: Several #mufc stars could be in international action tonight - find out who's involved: https://t.co/u097EazN0G", u'score': 237}, {u'text': u'RT @alice_powerx: How time flies @brooklynbeckham @ManUtd @UNICEF #MatchForChildren https://t.co/Cef52IfrVN', u'score': 175}]}

	return render(request, 'hue/home.html', context)

@transaction.atomic
def about(request):
  context = {}
  return render(request, 'hue/about.html', context)
