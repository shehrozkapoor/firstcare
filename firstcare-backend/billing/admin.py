from django.contrib import admin

from .models import *



admin.site.register(Billing)
admin.site.register(PaymentType)
admin.site.register(PaymentMethod)
admin.site.register(Payment)
admin.site.register(PaymentProfile)
admin.site.register(OnsetDataType)
admin.site.register(OtherDateType)
admin.site.register(HcfaBOX)
admin.site.register(ICD10)
admin.site.register(ICD9)
admin.site.register(CPTITEM)
admin.site.register(CPTCODE)
admin.site.register(HCPCS)
admin.site.register(HCPCSCODE)