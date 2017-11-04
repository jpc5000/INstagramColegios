from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    url(r'^$', views.signup, name='signup'),
    url(r'signin/$', auth_views.LoginView.as_view(template_name='signin.html',redirect_authenticated_user=True), name='signin'),
    url(r'signout/$', auth_views.LogoutView.as_view(), name='signout'),
    url(r'^index/$', views.index, name='index'),
    url(r'^profile/$', views.profile, name='profile'),
]
