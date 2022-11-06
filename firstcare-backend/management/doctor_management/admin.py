import imp
from pydoc import Doc
from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(Department)
admin.site.register(Doctor)