from django.contrib import admin

from blog.models import *

# admin se encarga de agragarlo
admin.site.register([categoria, post])

