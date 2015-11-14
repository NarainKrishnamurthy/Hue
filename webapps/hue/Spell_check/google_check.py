import json
import urllib2
import requests
from xml.etree import ElementTree


one = 'http://www.google.com/search?'
two = 'q=socer'
three = '&hl=en'
four = '&start=10'
five = '&num=10'
six  = '&output=xml'
seven= '&client=google-csbe'
eight= '&cx=00255077836266642015:u-scht7a-8i'

ulink= one + two + three+ four + five +six+seven + eight

print ulink

response = requests.get(ulink)

tree = ElementTree.fromstring(response.content)

print tree
