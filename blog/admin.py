from django.contrib import admin
from .models import Blogl
# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    pass

admin.site.register(Blogl,BlogAdmin)