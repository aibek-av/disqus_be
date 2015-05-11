"""This module contains DB models"""
from django.db import models
from django.utils import timezone
from core_app import utils
from hashlib import md5

class Comment(models.Model):

	author = models.CharField(max_length=1000)
	text = models.TextField()
	url = models.CharField(max_length=100)
	email = models.CharField(max_length=100)
	pub_date = models.DateTimeField(auto_now_add=timezone.now)