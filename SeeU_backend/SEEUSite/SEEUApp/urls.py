from django.conf.urls import url, include
import SEEUApp.views

#$正则表示结尾
urlpatterns = [
    url(r'add_user$',SEEUApp.views.add_user, ),
    url(r'show_users$', SEEUApp.views.show_users, ),
    url(r'user_register',SEEUApp.views.user_register),
    url(r'user_login$',SEEUApp.views.user_login),
    url(r'show_moments',SEEUApp.views.show_moments)
               ]