from django.conf.urls import url
from .import views

urlpatterns=[
    url(r'^submit/car/?$',views.submit_car,name='submit_car')
]