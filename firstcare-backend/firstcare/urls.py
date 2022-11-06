from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # admin panel url
    path('grappelli/', include('grappelli.urls')),
    path('admin/', admin.site.urls),
    # authentication app
    path('api/accounts/', include('accounts.urls')),
    #other modules
    path('patient/', include('Patient.urls')),
    path('management/', include('management.urls')),
    path('patienthealthcarerecord/', include('Patient_health_record.urls')),
    path('laboratory/', include('Laboratory.urls')),
    path('billing/', include('billing.urls')),
    # IMIS Inusrance
    path('insurance/', include('Insurance.urls')),
    path('drchronoinsurance/', include('drchrono_insurance.urls')),
    path('fhir/', include('FHIR.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
