from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import requests
def home(request):
	"""
	Home view
	"""
	url = 'https://api.github.com/orgs/jsshack15/repos?per_page=200'
	req = requests.get(url)
	# for i in req:
	# 	requests.get()
	template_name = 'index.html'
	# return HttpResponse(req.text)
	return render(request, template_name, {'content': req.json()})

