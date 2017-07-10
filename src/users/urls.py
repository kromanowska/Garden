from django.contrib.auth.views import login, logout_then_login, password_reset, password_reset_done, \
    password_reset_confirm, password_reset_complete
from django.conf.urls import url
from users import views

LOGIN = {
    'template_name': 'login.html',
    'redirect_authenticated_user': True
}
PASSWORD_RESET = {
    'template_name': 'password_reset.html',
    'email_template_name': 'password_reset_email.html',
    'post_reset_redirect': 'done/'
}
PASSWORD_RESET_DONE = {
    'template_name': 'password_reset_done.html'
}
RESET = {
    'template_name': 'password_reset_confirm.html',
    'post_reset_redirect': '../../done/'
}
RESET_DONE = {
    'template_name': 'password_reset_complete.html'
}

urlpatterns = [
    url(r'^login/$', login, LOGIN, name='login'),
    url(r'^logout/$', logout_then_login, name='logout'),
    url(r'^password-reset/$', password_reset, PASSWORD_RESET, name='password_reset'),
    url(r'^password-reset/done/$', password_reset_done, PASSWORD_RESET_DONE, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        password_reset_confirm, RESET, name='password_reset_confirm'),
    url(r'^reset/done/$', password_reset_complete, RESET_DONE, name='password_reset_complete'),

    url(r'^$', views.UserListView.as_view(), name='user_list'),
    url(r'^datatable/$', views.UserDataTableView.as_view(), name='user_list_datatable'),
    url(r'^create/$', views.UserCreateView.as_view(), name='user_create'),
    url(r'^update/(?P<pk>(\d)+)/$', views.UserUpdateView.as_view(), name='user_update'),
    url(r'^change-password/(?P<pk>(\d)+)/$', views.UserChangePasswordView.as_view(), name='user_change_password'),
    url(r'^delete/(?P<pk>(\d)+)/$', views.UserDeleteView.as_view(), name='user_delete'),
    url(r'^details/(?P<pk>(\d)+)/$', views.UserDetailView.as_view(), name='user_detail'),
]
