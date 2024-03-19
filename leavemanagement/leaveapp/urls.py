from django.urls import path
from . import views

urlpatterns=[
       path('',views.home,name='home'),
       path('about/',views.about,name='about'),
       path('contact/',views.contact,name='contact'),
       path('login/',views.login,name='login'),
       path('studentlog/',views.studentlog,name='studentlog'),
       path('studentlogin/',views.studentlogin,name='studentlogin'),
       path('studentprofile/',views.studentprofile,name='studentprofile'),
       path('studentupdate/<str:name>',views.studentupdate,name='studentupdate'),
       path('studentleaverequest/',views.studentleaverequest,name='studentleaverequest'),
       path('Teacherlogin/',views.Teacherlogin,name='Teacherlogin'),
       path('Teacherlog/',views.Teacherlog,name='Teacherlog'),
       path('TeacherReg/',views.TeacherReg,name='TeacherReg'),
       path('Teacherprofile/',views.Teacherprofile,name='Teacherprofile'),
       path('Teacherupdate/<str:name>',views.Teacherupdate,name='Teacherupdate'),
       path('viewleaverequest/',views.viewleaverequest,name='viewleaverequest'),
       path('leaveapproval/<str:pk>',views.leaveapproval,name='leaveapproval'),
       path('approvalstatus/',views.approvalstatus,name='approvalstatus'),
       path('logoutuser/',views.logoutuser,name="logoutuser"),

       
]