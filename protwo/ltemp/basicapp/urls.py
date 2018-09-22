from django.conf.urls import url
from basicapp import views

#template taging
app_name= 'basicapp'

urlpatterns=[
    url('relative/',views.relative,name='relative'),
    url('other/',views.other,name='other'),
    url('base/',views.base,name='base'),
]
