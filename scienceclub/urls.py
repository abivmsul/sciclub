from django.urls import path
from . import views
#from .views import (requestSummary, requestConfirm, myRequest)

urlpatterns = [
  path('', views.home, name='home'),
  path('register', views.register, name='register'),
    path('sciclub', views.sciclub, name='sciclub'),
    path('comclub', views.comclub, name='comclub'),
      path('coordinator', views.coordinator, name='coordinator'),
]