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

        twitter.twitter_query(search_query)
        path = os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile(inspect.currentframe() ))[0],"datumbox")))
        file_p = path + '/TextClassification.jar'
        ifile  = cmd_subfolder + '/data.json'
        ofile  = path + '/sentiment.csv'
        os.system("java -jar "+ file_p + ' ' + ifile + ' ' + ofile)
        path = os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile(inspect.currentframe() ))[0],"semantic-similarity-master")))
        cofile = path + '/senti.json'
        os.system(path + "/similar" + ' ' + ifile + ' ' + ofile + ' ' + cofile)
        with open(cofile) as data_file:
            data = json.load(data_file)
        context['data'] = data

	return render(request, 'hue/home.html', context)

@transaction.atomic
def about(request):
  context = {}
  return render(request, 'hue/about.html', context)
