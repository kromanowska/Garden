from django.conf.urls import url
from evaluations import views

urlpatterns = [
    url(r'^create/(?P<pk>(\d)+)/$', views.EvaluationCreateView.as_view(), name='evaluation_create'),
]
