from django.urls import path
from . import views
#from .views import (requestSummary, requestConfirm, myRequest)

urlpatterns = [
  path('login', views.login, name='login'),
  path('logout', views.logout, name='logout'),
]