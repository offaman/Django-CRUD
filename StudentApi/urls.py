from django.urls import path
from StudentApi import views 

urlpatterns =[
    path('student',views.studentInfo),
    path('student/<int:id>',views.studentInfo)
]