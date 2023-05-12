from django.contrib import admin
from .models import User, NewTweet, Profile

# Register your models here.
admin.site.register(User)
admin.site.register(NewTweet)
admin.site.register(Profile)