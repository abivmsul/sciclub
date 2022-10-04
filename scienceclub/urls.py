from django.urls import path
from . import views
#from .views import (requestSummary, requestConfirm, myRequest)

urlpatterns = [
  path('', views.home, name='home'),
  path('register', views.register, name='register'),
]