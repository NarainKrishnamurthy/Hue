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
import sys, os 
#import Twitter.twitter 

from hue.models import *



def home(request):
	context = {}
	#twitter_query(search_query)
	if request.method == 'GET':
		return render(request, 'hue/home.html', context)
		
	print request.POST

	#twitter_query(search_query)
	# sys call java file
	# c file return json
	# context['data'] = c file return value
	return render(request, 'hue/home.html', context)

def about(request):
  context = {}
  return render(request, 'hue/about.html', context)

def result(request):
  context = {}
  context['search_query'] = request.POST['search_q']
  return render(request, 'hue/result.html', context)