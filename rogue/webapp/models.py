from django.db import models

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