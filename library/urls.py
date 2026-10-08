from django.urls import path
from . import views
urlpatterns=[
 path('',views.dashboard,name='dashboard'), path('login/',views.login_view,name='login'), path('logout/',views.logout_view,name='logout'),
 path('books/',views.books,name='books'), path('members/',views.members,name='members'), path('circulation/',views.circulation,name='circulation'),
 path('rfid/',views.rfid,name='rfid'), path('migration/',views.migration,name='migration'), path('reports/',views.reports,name='reports'), path('health/',views.health,name='health'),
 path('demo/run/<int:scenario>/',views.run_scenario,name='run_scenario')]
