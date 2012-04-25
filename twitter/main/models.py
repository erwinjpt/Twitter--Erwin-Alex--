from django.db import models

class Customer(models.Model):
	image_customer =  models.ImageField(upload_to="img")
	name_customer = models.CharField(max_length=40)
	last_name_customer = models.CharField(max_length=15)
	birthday = models.DateField('Birth Date')
	location = models.CharField(max_length=30)

	def __unicode__(self):
		return 'Customer: %s - %s' % (self.pk, self.name_customer,)

class Tweet(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	Que_esta_pasando = models.CharField(max_length=100)
	name_customer = models.ForeignKey('Customer', related_name='tweet')

	def __unicode__(self):
		return 'Tweett: %s - %s' % (self.pk, self.Que_esta_pasando,)

class Bio(models.Model):
	name_customer = models.ForeignKey('Customer')
	hobbie = models.CharField(max_length=20)
	state = models.CharField(max_length=30)
	music = models.CharField(max_length=25)
	religion = models.CharField(max_length=20)
