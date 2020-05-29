from django.conf.urls import url, include
from SEEUApp.views import *
from django.urls import path

import SEEUApp
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'user_register',UserViewSet,basename="user-register")
router.register(r'add_moment',MomentCreateView,basename="moment-create")
router.register('user_login',UserLogViewSet,basename="user-login")
urlpatterns = [

    # url(r'user_login$',SEEUApp.views.user_login),
    # url(r'show_user/<int:id>',SEEUApp.views.show_userInfo),
    url(r'show_moment/',MomentPublishView.as_view(),name="moment-list"),
    url(r'users/',ShowUserView.as_view(),name='user-list'),
    path('show_user/<int:u_id>/',show_specific_user)
               ]
urlpatterns+=router.urls