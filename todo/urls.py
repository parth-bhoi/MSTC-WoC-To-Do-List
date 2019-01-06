from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name = 'index'),
    path('<int:Task_date_id>/',views.date_tasks,name ='date_tasks'),
    path('<int:Task_date_id>/complete/<int:Task_list_id>/',views.complete,name = 'complete'),
    path('<int:Task_date_id>/delcomplete/',views.delcomplete,name = 'delcomplete'),
    path('<int:Task_date_id>/delete/<Task_list_id>',views.deleteone,name = 'deleteone'),
    path('deldate/<int:Task_date_id>/',views.deldate,name = "deldate"),
    path('<int:Task_date_id>/delall/',views.delall,name = 'delall'),
]