from django.contrib import admin
from .models import Page, Product, UserProfile

admin.site.register(Product)

admin.site.register(Page)

admin.site.register(UserProfile)
    