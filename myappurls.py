in this file we need to create local urls of myapp

from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.index,name='index'), #^$ root url ,localhost 8000 ,yani jab localhost 8000 type hoga toh index template call hoga
    url(r'^test',views.test,name='test'),

]
