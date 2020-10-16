from django.contrib import admin
from .models import Task

# Register your models here.
admin.site.register(Task)


admin.site.site_header = "ToDo Admin"

admin.site.site_index = "ToDo Admin"

admin.site.site_title = "ToDo"