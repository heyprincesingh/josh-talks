from django.contrib import admin # type: ignore
from .models import User, Task

admin.site.register(User)
admin.site.register(Task)
