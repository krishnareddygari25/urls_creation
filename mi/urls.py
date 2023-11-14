from mi.views import *

from django.urls import path
app_name='something'

urlpatterns=[
    path('sharma/',sharma,name='sharma'),
    path('indian/',indian,name='indian'),
]