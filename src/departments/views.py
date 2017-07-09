from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from django.views.generic import TemplateView
from django_datatables_view.base_datatable_view import BaseDatatableView
from django.shortcuts import reverse
from django.db.models import Q
from common import enums
from departments import forms, models
from common.mixins import LoginSuperuserRequiredMixin


class DepartmentListView(LoginSuperuserRequiredMixin, TemplateView):
    template_name = 'department_list_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = forms.DepartmentsSearchForm()
        return context


class DepartmentDataTableView(LoginSuperuserRequiredMixin, BaseDatatableView):
    raise_exception = True
    model = models.Departments
    columns = ['name', 'abbreviation', 'is_active', 'manager', 'deputy_manager', 'urls']
    order_columns = ['name', 'abbreviation', 'is_active', 'manager', 'deputy_manager', '']
    max_display_length = 20

    def render_column(self, row, column):
        if column == 'is_active':
            return 'Active' if row.is_active else 'Inactive'
        elif column == 'manager':
            return row.manager.get_full_name()
        elif column == 'deputy_manager':
            return row.deputy_manager.get_full_name() if row.deputy_manager else ''
        elif column == 'urls':
            return {
                'update_url': reverse('departments:department_update', args=[row.id]),
                'delete_url': reverse('departments:department_delete', args=[row.id])
            }
        else:
            return super(DepartmentDataTableView, self).render_column(row, column)

    def filter_queryset(self, qs):
        qset = Q()

        name = self.request.POST.get('name')
        if name:
            qset &= Q(name__istartswith=name)

        abbreviation = self.request.POST.get('abbreviation')
        if abbreviation:
            qset &= Q(abbreviation__istartswith=abbreviation)

        is_active = self.request.POST.get('is_active')
        if is_active and int(is_active) == enums.IsActiveSearchEnum.ACTIVE:
            qset &= Q(is_active=True)
        elif is_active and int(is_active) == enums.IsActiveSearchEnum.INACTIVE:
            qset &= Q(is_active=False)

        manager = self.request.POST.get('manager')
        if manager:
            qset &= (Q(manager__first_name__istartswith=manager)
                     | Q(manager__last_name__istartswith=manager))

        deputy_manager = self.request.POST.get('deputy_manager')
        if deputy_manager:
            qset &= (Q(deputy_manager__first_name__istartswith=deputy_manager)
                     | Q(deputy_manager__last_name__istartswith=deputy_manager))

        return qs.filter(qset)


class DepartmentCreateView(LoginSuperuserRequiredMixin, CreateView):
    raise_exception = True
    model = models.Departments
    fields = ['name', 'abbreviation', 'manager', 'deputy_manager']
    template_name = 'department_create_view.html'
    success_url = reverse_lazy('departments:department_list')


class DepartmentUpdateView(LoginSuperuserRequiredMixin, UpdateView):
    raise_exception = True
    model = models.Departments
    fields = ['name', 'abbreviation', 'is_active', 'manager', 'deputy_manager']
    template_name = 'department_update_view.html'
    success_url = reverse_lazy('departments:department_list')


class DepartmentDeleteView(LoginSuperuserRequiredMixin, DeleteView):
    raise_exception = True
    model = models.Departments
    template_name = 'department_delete_view.html'
    success_url = reverse_lazy('departments:department_list')
