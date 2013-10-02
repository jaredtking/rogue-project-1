from django.contrib.auth.models import User, Group
from rest_framework import serializers
from rogue.webapp.models import *

class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields = ('url', 'username', 'email', 'groups')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Group
		fields = ('url', 'name')

class SocialMediaSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = SocialMedia
		fields = ('imageId', 'subject', 'platform', 'sender', 'content','installApp','needClick','fromFriend','trustLevel','enabled')

class EmailSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Email
		fields = ('imageId', 'subject', 'address', 'sender', 'date', 'content', 'containsPoorGrammar', 'containsHtml', 'containsImage', 'trustLevel', 'enabled') 

class WebpageSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Webpage
		fields = ('imageId', 'https', 'webAddress', 'title', 'content', 'containsPoorGrammar', 'containsImage', 'trustLevel', 'enabled')

class TrustDecisionSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = TrustDecision
		fields = ('user','decision', 'ctype', 'cid')
