from django.urls import path
from .views import *


urlpatterns = [
    path('category/',category,name="category"),
    path('dictionary/',dictionary,name="dictionary"),
    path('organizationtype/',organization_type,name="organization_type"),
    path('organization/',organization,name="organization"),
    path('panel/',panel,name="panel"),
    path('panelitem/',panel_item,name="panel_item"),
    path('resultlimit/',result_limit,name="resultlimit"),
    path('siteinformation/',site_information,name="site_information"),
    path('sampleentryconfig/',sample_entry_config,name="sample_entry_config"),
    path('printedreportsconfig/',printed_reports_config,name="printed_reports_config"),
    path('testresult/',test_result,name="test_result"),
    path('sampletypepanel/',sample_type_panel,name="sample_type_panel"),
    path('sampletypetest/',sample_type_test,name="sample_type_test"),
]
