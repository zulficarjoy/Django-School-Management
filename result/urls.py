from django.urls import path

from . import views


app_name = 'result'

urlpatterns = [
    path('', views.student_result, name='student_result'),
    path('create/', views.create_result.as_view(), name='create_result'),
]
