from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
  #sample urls for app

	url(r'^$', 'hue.views.home', name='home'),
	url(r'^home$', 'hue.views.home', name='home'),
  url(r'^about$', 'hue.views.about', name='about'),
  url(r'^result$', 'hue.views.result', name='result'),  
]
