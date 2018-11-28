from django.contrib import admin

# Register your models here.

from .models import report
from .models import DTE
from .models import personel


admin.site.register(report)
admin.site.register(DTE)
admin.site.register(personel)

