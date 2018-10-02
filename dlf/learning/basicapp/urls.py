from django.conf.urls import url
from basicapp import views
app_name = 'basicapp'
urlpatterns=[
    url('reg/',views.register,name='register'),
    url('login/',views.user_login,name='user_login'),
]
