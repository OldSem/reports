from django.contrib import admin

# Register your models here.

from .models import report
from .models import DTE
from .models import DPRS
from .models import OKS
from .models import ES
from .models import BUH
from .models import OV
from .models import OTL
from .models import personel
from .models import BTS

admin.site.register(report)
admin.site.register(DTE)
admin.site.register(DPRS)
admin.site.register(OKS)
admin.site.register(ES)
admin.site.register(BUH)
admin.site.register(OV)
admin.site.register(OTL)
admin.site.register(personel)
admin.site.register(BTS)
