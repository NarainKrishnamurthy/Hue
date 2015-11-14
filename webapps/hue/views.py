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


def home(request):
	context = {}

	if request.method == 'GET':
		return render(request, 'hue/home.html', context)

	search_query = request.POST['search_q']

	twitter.twitter_query(search_query)

	# sys call java file
	# c file return json
	# context['data'] = c file return value
	return render(request, 'hue/home.html', context)

def test(request):
  context = {}
  return render(request, 'hue/test.html', context)

