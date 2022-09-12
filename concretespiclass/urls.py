from django.urls import path
from .import views

urlpatterns=[
    path('studenthandle/',views.studentlistcreate.as_view()),


    path('studenthandle/<int:pk>', views.studentretrieveupdatedestroy.as_view()),


]