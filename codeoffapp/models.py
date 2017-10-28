from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	VOCAL='Vocal',
	INSTRUMENTAL='Instrumental',
	INTEREST_CHOICES = (
		(VOCAL,'Vocal'),
		(INSTRUMENTAL,'Instrumental'),

	)
	Interest = models.CharField(max_length=3,choices=INTEREST_CHOICES,
	default=VOCAL,)

	#user_pic=models.ImageField(upload_to='UserImages',blank=True)
	Folk='Folk',
	Jazz='Jazz',
	HipHop='HipHop',
	Rapping='Rapping',
	Classical='Classical',
	EDM='EDM',
	Rock='Rock',
	Disco='Disco',
	
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
	MENTOR='Mentor',
	MENTEE='MENTEE',
	INTEREST_CHOICES = (
		(MENTOR,'Mentor'),
		(MENTEE,'Mentee'),

	)
	Status = models.CharField(max_length=6,choices=INTEREST_CHOICES,
	default=MENTEE,)
	Score = models.IntegerField(default=0)


class Post(models.Model):
	user_posted = models.ForeignKey(Profile)
	post_text = models.CharField(max_length=500)
	File =models.FileField(upload_to = 'audio',blank=True)
	Posted_On = models.DateTimeField(auto_now=True)

