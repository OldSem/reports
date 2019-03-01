from django.contrib import admin

# Register your models here.

from .models import report
from .models import DTE
from .models import personel,Division,Dept,Work,Wtype,WorkCode


admin.site.register(report)
admin.site.register(DTE)
admin.site.register(personel)
admin.site.register(Division)
admin.site.register(Dept)
admin.site.register(Work)
admin.site.register(Wtype)
admin.site.register(WorkCode)
