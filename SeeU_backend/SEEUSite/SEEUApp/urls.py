from django.conf.urls import url, include
from SEEUApp.views import MomentPublishView,ShowUserView
import SEEUApp

urlpatterns = [
    url(r'add_user$',SEEUApp.views.add_user, ),
    url(r'user_register',SEEUApp.views.user_register),
    url(r'user_login$',SEEUApp.views.user_login),
    url(r'show_user/<int:id>',SEEUApp.views.show_userInfo),
    url(r'moment/',MomentPublishView.as_view(),name="moment-list"),
    url(r'users/',ShowUserView.as_view(),name='user-list')
               ]