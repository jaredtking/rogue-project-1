from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ContentItem(models.Model):
	"""
		This is a piece of content that will be stored to the database
		"""
	name = models.CharField(max_length=30, unique=True)
	itemType = models.CharField(max_length=30, default='generic')
	trustLevel = models.FloatField()
	enabled = models.BooleanField(default=True)
		# otherModelRefExample = models.ForeignKey(<other_model_class_name>, unique=True)
	# manyToManyExample = models.ManyToManyField('<other model name>')
		
	class Meta:
			#This will be used by the admin interface      
		verbose_name_plural = "ContentItems"
	
	class Admin:
			#This inner class indicates to the admin interface how to display a user
			#See the Django documentation for more information
		list_display = ('name', 'itemType', 'trustLevel', 'enabled')

	def toDict(self):
		"""
		Return a dictionary containing information about this content Item
		"""
		cItem = {
					'id': self.id,
					'name': self.name,
					'itemType':self.itemType,
					'trustLevel':self.trustLevel,
					'enabled':self.enabled,
				}
		return cItem

class SocialMedia(models.Model): 
		imageId = models.CharField(max_length=50) 
		subject = models.CharField(max_length=78, unique=True)
		platform = models.CharField(max_length=78)
		sender = models.CharField(max_length=75) 
		content = models.TextField()#Text field of contents
		installApp = models.BooleanField(default=False) 
		needClick = models.BooleanField(default=False) 
		fromFriend = models.BooleanField(default=False) 
		trustLevel = models.FloatField() 
		enabled = models.BooleanField(default=True) 
		
		class Meta:   
			verbose_name_plural = "Social Media Elements"
	
		class Admin:
			#This inner class indicates to the admin interface how to display a user
			#See the Django documentation for more information
			list_display = ('imageId', 'subject', 'platform', 'sender', 'content','installApp','needClick','fromFriend','trustLevel','enabled')

		def toDict(self):
			sItem = {
				'imageId':self.imageId, 
				'subject': self.subject,
				'platform': self.platform,
				'sender':self.sender,
				'content':self.content,
				'installApp':self.installApp,
				'needClick':self.needClick,
				'fromFriend':self.fromFriend,
				'trustLevel':self.trustLevel, 
				'enabled':self.enabled,
				}
			return sItem

class Email(models.Model): 
		imageId = models.CharField(max_length=50) 
		subject = models.CharField(max_length=78, unique=True) 
		address = models.EmailField(max_length=254) 
		sender = models.CharField(max_length=75) 
		date = models.DateField() 
		content = models.TextField() 
		containsPoorGrammar = models.BooleanField(default=False) 
		containsHtml = models.BooleanField(default=False) 
		containsImage = models.BooleanField(default=False) 
		trustLevel = models.FloatField() 
		enabled = models.BooleanField(default=True)

		class Meta:   
			verbose_name_plural = "Email Elements"

		class Admin:
			list_display = ('imageId', 'subject', 'address', 'sender', 'date', 'content', 'containsPoorGrammar', 'containsHtml', 'containsImage', 'trustLevel', 'enabled') 

		def toDict(self):
			eItem = {
				'imageId':self.imageId, 
				'subject': self.subject,
				'address': self.address,
				'sender':self.sender,
				'date':self.date,
				'content':self.content,
				'containsPoorGrammar':self.containsPoorGrammar,
				'containsHtml':self.containsHtml,
				'containsImage':self.containsImage,
				'trustLevel':self.trustLevel, 
				'enabled':self.enabled,
				}
			return eItem

class Webpage(models.Model): 
		imageId = models.CharField(max_length=50) 
		https = models.BooleanField(default=False) 
		webAddress = models.TextField() 
		title = models.CharField(max_length=75)
		content = models.TextField() 
		containsPoorGrammar = models.BooleanField(default=False) 
		containsImage = models.BooleanField(default=False) 
		trustLevel = models.FloatField() 
		enabled = models.BooleanField(default=True) 

		class Meta:   
			verbose_name_plural = "Webpage Elements"

		class Admin:
			list_display = ('imageId', 'https', 'webAddress', 'title', 'content', 'containsPoorGrammar', 'containsImage', 'trustLevel', 'enabled') 

		def toDict(self):
			wItem = {
				'imageId':self.imageId, 
				'https': self.https,
				'webAddress': self.webAddress,
				'title':self.title,
				'content':self.content,
				'containsPoorGrammar':self.containsPoorGrammar,
				'containsImage':self.containsImage,
				'trustLevel':self.trustLevel, 
				'enabled':self.enabled,
				}
			return wItem

class TrustDecision(models.Model):
		user = models.ForeignKey(User)
		decision = models.BooleanField(default=True)

		class Meta:   
			verbose_name_plural = "Trust Decisions"

		class Admin:
			list_display = ('user','decision')

		def toDict(self):
			tdItem = {
				'user': self.user,
				'decision': self.decision
				}
			return tdItem