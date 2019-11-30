from django.urls import path
from . import views


app_name = 'admin_tools'

urlpatterns = [
    # Semester
    path('semesters/', views.semesters, name='all_semester'),
    path('departments/', views.departments, name='departments'),
    path('combinations/', views.combination_list.as_view(), name='combinations'),
    path('academic_sessions/', views.academic_session, name='academic_sessions'),
    path('combinations/add/', views.create_combination.as_view(),
         name='create_combination'),
]
