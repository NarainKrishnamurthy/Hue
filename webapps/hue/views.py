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
cmd_subfolder  = os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile(inspect.currentframe() ))[0],"sentiment")))
if cmd_subfolder not in sys.path:
     sys.path.insert(0, cmd_subfolder)

cmd_subfolder_t  = os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile(inspect.currentframe() ))[0],"Twitter")))
if cmd_subfolder_t not in sys.path:
     sys.path.insert(0, cmd_subfolder_t)

cmd_subfolder_r  = os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile(inspect.currentframe() ))[0],"Reddit")))
if cmd_subfolder_r not in sys.path:
     sys.path.insert(0, cmd_subfolder_r)

import twitter
import sentiment
from RedditParser import RedditParser


def twitter_posts(query):
  twitter.twitter_query(query)

  path = os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile(inspect.currentframe() ))[0],"datumbox")))
  ifile  = cmd_subfolder_t + '/data.json'
  ofile  = path + '/sentiment.csv'

  print ifile
  print ofile

  sentiment.analyze_sentiment(ifile, ofile, 0.1)

  path = os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile(inspect.currentframe() ))[0],"semantic-similarity-master")))
  cofile = path + '/senti.json'
  os.system(path + "/similar" + ' ' + ifile + ' ' + ofile + ' ' + cofile)
  with open(cofile) as data_file:
      data = json.load(data_file)
  return json.dumps(data)

def reddit_posts(query):
  r = RedditParser()
  r.reddit_query(query, 25, 25)
  path = os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile(inspect.currentframe() ))[0],"datumbox")))
  ifile  = cmd_subfolder_r + '/data.json'
  ofile  = path + '/sentiment.csv'

  sentiment.analyze_sentiment(ifile, ofile, 0.1)
  path = os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile(inspect.currentframe() ))[0],"semantic-similarity-master")))
  cofile = path + '/reddit_senti.json'
  os.system(path + "/similar" + ' ' + ifile + ' ' + ofile + ' ' + cofile)
  with open(cofile) as data_file:
      data = json.load(data_file)
  return json.dumps(data)


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
    context['query'] = True

    jtdumps = twitter_posts(search_query);
    jrdumps = reddit_posts(search_query);

    context['data_tw'] = jtdumps
    context['data_re'] = jrdumps

  return render(request, 'hue/home.html', context)

@transaction.atomic
def about(request):
  context = {}
  return render(request, 'hue/about.html', context)
