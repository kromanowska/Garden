from django.contrib import admin
from django.conf.urls import url, include
from garden import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('users.urls', namespace='users')),
    url(r'^evaluations/', include('evaluations.urls', namespace='evaluations')),
    url(r'^departments/', include('departments.urls', namespace='departments')),
    url(r'^files/(?P<path>.*)', views.FileView.as_view(), name='file'),
]
