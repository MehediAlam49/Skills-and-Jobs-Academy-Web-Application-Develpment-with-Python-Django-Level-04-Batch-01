from django.contrib import admin
from news_portal_app.models import *

# Register your models here.
admin.site.register([CustomUserModel, newsModel])