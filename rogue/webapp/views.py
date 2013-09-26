# Import http functionality
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import Context, RequestContext, loader
from django.shortcuts import render_to_response, get_object_or_404
from django.template.loader import render_to_string

# Import models
from django.db import models
from django.contrib.auth.models import User
from rogue.webapp.models import *

# Import helper functions
from django.contrib.auth import authenticate as auth_func
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib import messages
from django import forms

#Added Rest API functionality from Django REST
from rest_framework import viewsets
from rogue.webapp.serializers import *
from django.contrib.auth.models import User,Group

# Create your views here.
def home(request):
  """
  Default controller for handling requests to /
  This method only serves the index.html file.
  """
  
  return render_to_response('index.html',
                {}, RequestContext(request))

def foo(request, foo_bar):
  """
  Controller for handling requests to /foo/<foo_bar>
  """
  #do a foo calculation
  foo_result = int(foo_bar) + 7
  return render_to_response('demo/foo.html',
                {'input':foo_bar,
			     'result':foo_result}, RequestContext(request))

def getContentItem(request, item_name):
  """
  Controller for getting a content item by name, handles requests to /cItem/<name>
  """
  #check to see if item exists, if not 404
  content_item = get_object_or_404(ContentItem, name = item_name)
  return render_to_response('demo/cItem.html',
                {'item_dict':content_item.toDict()}, RequestContext(request))

# Render content models
def getSocialMediaItem(request, item_name):
  """
  Controller for getting a content item by name, handles requests to /_Item/<name>
  """
  #check to see if item exists, if not 404
  content_item = get_object_or_404(SocialMedia, imageId = item_name)
  return render_to_response('content/view.html',
                {
                  'item_dict':content_item.toDict(),
                  'content_type':'socialmedia'}, RequestContext(request))
def getEmailItem(request, item_name):
  """
  Controller for getting a content item by name, handles requests to /_Item/<name>
  """
  #check to see if item exists, if not 404
  content_item = get_object_or_404(Email, imageId = item_name)
  return render_to_response('content/view.html',
                {
                  'item_dict':content_item.toDict(),
                  'content_type':'email'}, RequestContext(request))
def getWebpageItem(request, item_name):
  """
  Controller for getting a content item by name, handles requests to /_Item/<name>
  """
  #check to see if item exists, if not 404
  content_item = get_object_or_404(Webpage, imageId = item_name)
  return render_to_response('content/view.html',
                {
                  'item_dict':content_item.toDict(),
                  'content_type':'webpage'}, RequestContext(request))

#render the ember app
def emberhome(request):
    """
    Default controller for handling requests to /ember
    This method only serves the ember.html file.
    """

    return render_to_response('ember.html', {}, RequestContext(request))

class UserViewSet(viewsets.ModelViewSet):
    """
    Views that allow users to be viewed or edited via RESTful API
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    Views that allow groups to be viewed or edited via RESTful API
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class SocialMediaViewSet(viewsets.ModelViewSet):
    """
    Views that allow socialmedia to be viewed or edited via RESTful API
    """
    queryset = SocialMedia.objects.all()
    serializer_class = SocialMediaSerializer

class EmailViewSet(viewsets.ModelViewSet):
    """
    Views that allow Emails to be viewed or edited via RESTful API
    """
    queryset = Email.objects.all()
    serializer_class = EmailSerializer

class WebpageViewSet(viewsets.ModelViewSet):
    """
    Views that allow Webpages to be viewed or edited via RESTful API
    """
    queryset = Webpage.objects.all()
    serializer_class = WebpageSerializer

def startQuiz(request):
    """
    Route for starting the quiz. Ember provides the
    templating.
    """
    return render_to_response('quiz.html', {}, RequestContext(request))

def generateQuiz(request):
    """
    Route for generating the quiz. Returns JSON.
    """

    # grab N random content ids from various types
    # TODO

    return HttpResponse('{"quiz":[{"contentitem_type":"email","contentitem_id":1}]}', mimetype="application/json")