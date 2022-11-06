from django.contrib import admin
from .models import *


admin.site.register(CoverageEligibilityBundle)
admin.site.register(PreAuthBundle)
admin.site.register(ClaimBundle)
admin.site.register(CommunicationBundle)
admin.site.register(PaymentReconciliationBundle)
admin.site.register(PaymentNoticeBundle)
admin.site.register(TaskBundle)
admin.site.register(DiagnosisInformation)
admin.site.register(SupportingInfo)
admin.site.register(CareTeam)
admin.site.register(Items)
admin.site.register(Claim)