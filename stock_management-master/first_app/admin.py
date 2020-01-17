from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.User1)
# admin.site.register(models.Logins)
admin.site.register(models.Books)
admin.site.register(models.Electronics)
admin.site.register(models.Sports)
admin.site.register(models.Courses)
admin.site.register(models.StoreManager)
admin.site.register(models.Stores)
admin.site.register(models.Shopping_Basket)