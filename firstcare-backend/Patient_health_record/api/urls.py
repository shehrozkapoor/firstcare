from unicodedata import name
from django.urls import path
from .views import *



urlpatterns = [
    path('dosageinstruction/',dosage_instruction,name="dosage_instruction"),
    path('relationship/',relation_ship,name="relation_ship"),
    path('encountertype/',encounter_type,name="encounter_type"),
    path('chiefcomplain/',chief_complain,name="chief_complain"),
    path('vitalsigns/',vital_signs,name="vital_signs"),
    path('problems/',problems,name="problems"),
    path('problemlist/',problem_list,name="problem_list"),
    path('document/',document,name="document"),
    path('historytype/',history_type,name="history_type"),
    path('history/',history,name="history"),
    path('reviewofsystem/',review_of_system,name="review_of_system"),
    path('physicalexam/',physical_exam,name="physical_exam"),
    path('order/',order,name="order"),
    path('assessmentandplan/',assessment_and_plan,name="assessment_and_plan"),
    path('progressnote/',progress_note,name="progress_note"),
    path('encounter/',encounter,name="encounter"),
]