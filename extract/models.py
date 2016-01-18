from django.db import models

# Create your models here.
class MetaInfo(models.Model):
	title = models.CharField(max_length=500,blank = False)
	description = models.CharField(max_length=1000,blank = True)
	keywords = models.CharField(max_length=500,blank = True)

	def __unicode__(self):
		return self.title
