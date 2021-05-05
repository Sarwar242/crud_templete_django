from django.urls import path
from . import views
from .views import Addsub, Addstudent, StudentUpdate, StudentDetail, StudentDelete


urlpatterns = [
    path('api/',views.studentList, name='studentlistapi'),
    path('api/student/',views.studentList, name='studentlistapi'),
    path('api/subject/',views.subjectList, name='subjectlistapi'),
    path('api/student/<str:pk>/',views.studentJust, name='studentdetailapi'),
    path('api/subject/<str:pk>/',views.subjectJust, name='subjectdetailapi'),
    path('api/student/add/',views.studentAdd, name='studentaddapi'),
    path('api/add/',views.subjectAdd, name='subjectaddapi'),
    path('api/student/update/<str:pk>/',views.studentUpdate, name='studentupdateapi'),
    path('api/subject/update/<str:pk>/',views.subjectUpdate, name='subjectupdateapi'),
    path('api/student/delete/<str:pk>/',views.studentDelete, name='studentdeleteapi'),
    path('api/subject/delete/<str:pk>/',views.subjectDelete, name='subjectdeleteapi'),
    
    path('', views.index, name='index'),
    path('app/', views.app, name='app'),
    path('addsub/', Addsub.as_view(), name='addsub'),
    path('sub/<int:pk>/', views.SubDetail.as_view(), name='subject'),
    path('subupdate/<int:pk>/', views.SubUpdate.as_view(), name='updatesub'),
    path('subdelete/<int:pk>/', views.SubDelete.as_view(), name='deletesub'),
    path('addstudent/', Addstudent.as_view(), name='addstudent'),
    path('student/<int:pk>/', StudentDetail.as_view(), name='student'),
    path('student/<int:pk>/update/', StudentUpdate.as_view(), name='studentupdate'),
    path('student/<int:pk>/delete/', StudentDelete.as_view(), name='studentdelete'),
]

# urlpatterns+=[
    
# ]