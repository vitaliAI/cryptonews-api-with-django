from django.contrib import admin

# Register your models here.
from .models import CryptoNews


@admin.register(CryptoNews)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'sentiment', 'source')
    list_filters = ('source', 'sentiment')
