from django.conf.urls import url
from departments import views

urlpatterns = [
    url(r'^$', views.DepartmentListView.as_view(), name='department_list'),
    url(r'^datatable/$', views.DepartmentDataTableView.as_view(), name='department_list_datatable'),
    url(r'^create/$', views.DepartmentCreateView.as_view(), name='department_create'),
    url(r'^update/(?P<pk>(\d)+)/$', views.DepartmentUpdateView.as_view(), name='department_update'),
    url(r'^delete/(?P<pk>(\d)+)/$', views.DepartmentDeleteView.as_view(), name='department_delete'),

]
