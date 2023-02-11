from django.urls import path
from app import views

urlpatterns = [
    path('stuinfo/<int:pk>',views.student_detail),
    path('stuinfo/',views.student_list),
]
