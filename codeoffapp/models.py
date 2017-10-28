from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	VOCAL='Vo',
	INSTRUMENTAL='Ins',
	INTEREST_CHOICES = (
		(VOCAL,'Vocal'),
		(INSTRUMENTAL,'Instrumental'),

	)
	Interest = models.CharField(max_length=3,choices=INTEREST_CHOICES,
	default=VOCAL,)

	#user_pic=models.ImageField(upload_to='UserImages',blank=True)
	Folk='Fo',
	Jazz='Ja',
	HipHop='Hi',
	Rapping='Rap',
	Classical='Cl',
	EDM='Ed',
	Rock='Ro',
	Disco='Di',
	
	genre=(
	(Folk, 'Folk'),
	(Jazz, 'Jazz'),
	(HipHop, 'HipHop'),
	(Rapping, 'Rapping'),
	(Classical, 'Classical'),
	(EDM, 'EDM'),
	(Rock, 'Rock'),
	(Disco, 'Disco'),

	)

	Genre = models.CharField(max_length=3,choices=genre,
	default=Classical,)
	Associated_with= models.CharField(max_length=32)

class post(models.Model):
	user_posted = models.OneToOneField(Profile),
	Post = models.CharField(max_length=500),
	File =models.FileField(upload_to = 'music'),
	Posted_On = models.DateField(auto_now=True)

