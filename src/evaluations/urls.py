from django.conf.urls import url
from evaluations import views

urlpatterns = [
    url(r'^$', views.EvaluationListView.as_view(), name='evaluation_list'),
    url(r'^datatable/$', views.EvaluationDataTableView.as_view(), name='evaluation_list_datatable'),
    url(r'^datatable-user/(?P<pk>(\d)+)/$', views.EvaluationUserDataTableView.as_view(),
        name='evaluation_list_datatable_user'),
    url(r'^detail/(?P<pk>(\d)+)/$', views.EvaluationDetailView.as_view(), name='evaluation_detail'),
    url(r'^create/(?P<pk>(\d)+)/$', views.EvaluationCreateView.as_view(), name='evaluation_create'),
    url(r'^update/(?P<pk>(\d)+)/$', views.EvaluationUpdateView.as_view(), name='evaluation_update'),
    url(r'^delete/(?P<pk>(\d)+)/$', views.EvaluationDeleteView.as_view(), name='evaluation_delete'),
]
