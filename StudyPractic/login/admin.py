from django.contrib import admin
from .models import CustomUser, UserHistory, User
# Register your models here.
admin.site.register(CustomUser)
admin.site.register(UserHistory)
admin.site.register(User)