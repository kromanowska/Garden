from django.contrib.auth import models as auth_models
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from django.views.generic import TemplateView
from django_datatables_view.base_datatable_view import BaseDatatableView
from django.shortcuts import reverse
from django.db.models import Q
from common import enums
from users import forms, models
from common.mixins import LoginSuperuserRequiredMixin


class UserListView(LoginRequiredMixin, TemplateView):
    template_name = 'user_list_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = forms.UserSearchForm()
        return context


class UserDataTableView(LoginSuperuserRequiredMixin, BaseDatatableView):
    raise_exception = True
    model = auth_models.User
    columns = ['first_name', 'last_name', 'email', 'profile__landline_phone',
               'profile__cell_phone', 'profile__department__name', 'is_active', 'urls']
    order_columns = ['first_name', 'last_name', 'email', 'profile__landline_phone',
                     'profile__cell_phone', 'profile__department__name', 'is_active', '']
    max_display_length = 20

    def get_initial_queryset(self):
        return super().get_initial_queryset() \
            .filter(profile__isnull=False) \
            .select_related('profile', 'profile__department')

    def render_column(self, row, column):
        if column == 'is_active':
            return 'Active' if row.is_active else 'Inactive'
        elif column == 'profile__landline_phone':
            return str(row.profile.landline_phone)
        elif column == 'profile__cell_phone':
            return str(row.profile.cell_phone)
        elif column == 'profile__department__name':
            return row.profile.department.name
        elif column == 'urls':
            return {
                # 'update_url': reverse('departments:department_update', args=[row.id]),
                # 'delete_url': reverse('departments:department_delete', args=[row.id])
            }
        else:
            return super(UserDataTableView, self).render_column(row, column)

    def filter_queryset(self, qs):
        qset = Q()

        name = self.request.POST.get('name')
        if name:
            qset &= (Q(first_name__istartswith=name) | Q(last_name__istartswith=name))

        email = self.request.POST.get('email')
        if email:
            qset &= Q(email__istartswith=email)

        phone = self.request.POST.get('phone')
        if phone:
            qset &= (Q(profile__landline_phone__istartswith=phone)
                     | Q(profile__cell_phone__istartswith=phone))

        department = self.request.POST.get('department')
        if department:
            qset &= Q(profile__department_id=department)

        is_active = self.request.POST.get('is_active')
        if is_active and int(is_active) == enums.IsActiveSearchEnum.ACTIVE:
            qset &= Q(is_active=True)
        elif is_active and int(is_active) == enums.IsActiveSearchEnum.INACTIVE:
            qset &= Q(is_active=False)

        return qs.filter(qset)

# class DepartmentCreateView(LoginSuperuserRequiredMixin, CreateView):
#     raise_exception = True
#     model = models.Departments
#     fields = ['name', 'abbreviation', 'manager', 'deputy_manager']
#     template_name = 'department_create_view.html'
#     success_url = reverse_lazy('departments:department_list')
#
#
# class DepartmentUpdateView(LoginSuperuserRequiredMixin, UpdateView):
#     raise_exception = True
#     model = models.Departments
#     fields = ['name', 'abbreviation', 'is_active', 'manager', 'deputy_manager']
#     template_name = 'department_update_view.html'
#     success_url = reverse_lazy('departments:department_list')
#
#
# class DepartmentDeleteView(LoginSuperuserRequiredMixin, DeleteView):
#     raise_exception = True
#     model = models.Departments
#     template_name = 'department_delete_view.html'
#     success_url = reverse_lazy('departments:department_list')
