from django.urls import path
from . import views


urlpatterns = [
    path('', views.home,name="home_student"),
    path('del/<str:s_roll>/', views.student_del , name="del_stu"),
    path('edit_stu/<str:s_roll>/', views.edit_stu , name="edit_stu"),
    path('create/', views.create_stu , name="create_stu"),


    path('all_results', views.all_results,name="all_results"),
    path('del_result/<str:s_roll>/', views.result_del , name="result_del"),
    path('edit_result/<int:id>/', views.edit_result , name="edit_result"),
    path('create_result/', views.create_result , name="create_result"),
]
