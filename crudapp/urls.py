from django.urls import path
from . import views
from .views import Addsub, Addstudent, StudentUpdate, StudentDetail, StudentDelete


urlpatterns = [
    path('api/',views.studentList, name='studentlistapi'),
    path('api/students/',views.studentList, name='studentlistapi'),
    path('api/subjects/',views.subjectList, name='subjectlistapi'),
    path('api/studentadd/',views.studentAdd.as_view()),
    path('api/subjectadd/',views.subjectAdd.as_view()),
    path('api/studentops/<int:pk>/',views.studentOperationsApi.as_view()),
    path('api/subjectops/<int:pk>/',views.subjectOperationsApi.as_view()),
    # path('api/student/<str:pk>/',views.studentJust, name='studentdetailapi'),
    # path('api/subject/<str:pk>/',views.subjectJust, name='subjectdetailapi'),
    # path('api/subjectadd/',views.subjectAdd, name='subjectaddapi'),
    # path('api/subjectupdate/<str:pk>/',views.subjectUpdate, name='subjectupdateapi'),
    # path('api/studentdelete/<str:pk>/',views.studentDelete, name='studentdeleteapi'),
    # path('api/subjectdelete/<str:pk>/',views.subjectDelete, name='subjectdeleteapi'),

    path('app/', views.app, name='app'),
    path('addsub/', Addsub.as_view(), name='addsub'),
    path('sub/<int:pk>/', views.SubDetail.as_view(), name='subject'),
    path('subupdate/<int:pk>/', views.SubUpdate.as_view(), name='updatesub'),
    path('subdelete/<int:pk>/', views.SubDelete.as_view(), name='deletesub'),
    path('addstudent/', Addstudent.as_view(), name='addstudent'),
    path('student/<int:pk>/', StudentDetail.as_view(), name='student'),
    path('student/<int:pk>/update/', StudentUpdate.as_view(), name='studentupdate'),
    path('student/<int:pk>/delete/', StudentDelete.as_view(), name='studentdelete'),
    path('', views.index, name='index'),
]

# urlpatterns+=[
    
# ]