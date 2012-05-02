from django.db import models

class Tweet(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	Que_esta_pasando = models.CharField(max_length=100)
	name_customer = models.ForeignKey('auth.User', related_name='tweet')

	def __unicode__(self):
		return 'Tweett: %s - %s' % (self.pk, self.Que_esta_pasando,)

class UserProfile(models.Model):
	image_customer =  models.ImageField(upload_to="img")
	user = models.OneToOneField('auth.User')
	last_name = models.CharField(max_length=15)
	birthday = models.DateField('Birth Date')
	location = models.CharField(max_length=30)
