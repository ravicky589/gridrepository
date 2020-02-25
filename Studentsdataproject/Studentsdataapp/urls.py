from django.urls import path
from Studentsdataapp import views

urlpatterns = [
    path('',views.home_view, name='home'),
    path('add_student/',views.add_student_view,name = 'add_student'),
    path('create/',views.inserting_data_view, name='create'),
    path('edit/<pk>',views.updating_data_view,name='update'),
    path('update/<pk>',views.replacing_data_view,name = 'replace'),
    path('delete/<pk>',views.deleting_data_view,name='delete')
]
