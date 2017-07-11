from django_datatables_view.base_datatable_view import BaseDatatableView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth import models as auth_models
from django.contrib.auth import forms as auth_forms
from django.views.generic import TemplateView, FormView, DeleteView, View, DetailView
from django import shortcuts
from django.urls import reverse_lazy
from django.db import transaction
from django.db.models import Q
from common.mixins import LoginSuperuserRequiredMixin
from common import enums
from users import forms


class UserListView(LoginRequiredMixin, TemplateView):
    template_name = 'user_list_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = forms.UserSearchForm()
        return context


class UserDataTableView(LoginRequiredMixin, BaseDatatableView):
    raise_exception = True
    model = auth_models.User
    columns = ['first_name', 'last_name', 'profile__job', 'email', 'phone',
               'profile__department__name', 'urls']
    order_columns = ['first_name', 'last_name', 'profile__job', 'email', '',
                     'profile__department__name', '']
    max_display_length = 20

    def get_initial_queryset(self):
        return super().get_initial_queryset() \
            .filter(profile__isnull=False) \
            .select_related('profile', 'profile__department')

    def render_column(self, row, column):
        if column == 'profile__job':
            return row.profile.job
        elif column == 'phone':
            return {
                'landline_phone': str(row.profile.landline_phone),
                'cell_phone': str(row.profile.cell_phone)
            }
        elif column == 'profile__department__name':
            return row.profile.department.name
        elif column == 'urls':
            urls = {
                'detail_url': shortcuts.reverse('users:user_detail', args=[row.id]),
            }
            if self.request.user.is_superuser:
                urls['change_password_url'] = shortcuts.reverse('users:user_change_password', args=[row.id]),
                urls['update_url'] = shortcuts.reverse('users:user_update', args=[row.id]),
                urls['delete_url'] = shortcuts.reverse('users:user_delete', args=[row.id])
            elif self.request.user.id == row.id:
                urls['change_password_url'] = shortcuts.reverse('users:user_change_password', args=[row.id]),
            return urls
        else:
            return super().render_column(row, column)

    def filter_queryset(self, qs):
        qset = Q()

        name = self.request.POST.get('name')
        if name:
            qset &= (Q(first_name__istartswith=name) | Q(last_name__istartswith=name))

        job = self.request.POST.get('job')
        if job:
            qset &= Q(profile__job__istartswith=job)

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


class UserDetailView(LoginRequiredMixin, DetailView):
    raise_exception = True
    model = auth_models.User
    template_name = 'user_detail_view.html'


class UserCreateView(LoginSuperuserRequiredMixin, View):
    raise_exception = True
    template_name = 'user_create_view.html'

    def get(self, request, *args, **kwargs):
        context = {
            'user_form': forms.UserCreateForm(),
            'profile_form': forms.ProfileForm()
        }
        return shortcuts.render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        user_form = forms.UserCreateForm(request.POST)
        profile_form = forms.ProfileForm(request.POST, request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            with transaction.atomic():
                user_form.save()
                profile_form.instance.user = user_form.instance
                profile_form.save()
            return shortcuts.redirect('users:user_detail', pk=user_form.instance.id)
        else:
            context = {
                'user_form': user_form,
                'profile_form': profile_form
            }
            return shortcuts.render(request, self.template_name, context)


class UserUpdateView(LoginSuperuserRequiredMixin, View):
    raise_exception = True
    template_name = 'user_update_view.html'

    def get(self, request, pk, *args, **kwargs):
        user = shortcuts.get_object_or_404(auth_models.User, pk=pk, profile__isnull=False)
        context = {
            'user_form': forms.UserUpdateForm(instance=user),
            'profile_form': forms.ProfileForm(instance=user.profile)
        }
        return shortcuts.render(request, self.template_name, context)

    def post(self, request, pk, *args, **kwargs):
        user = shortcuts.get_object_or_404(auth_models.User, pk=pk, profile__isnull=False)
        user_form = forms.UserUpdateForm(request.POST, instance=user)
        profile_form = forms.ProfileForm(request.POST, request.FILES, instance=user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            with transaction.atomic():
                user_form.save()
                profile_form.save()
            return shortcuts.redirect('users:user_detail', pk=user_form.instance.id)
        else:
            context = {
                'user_form': user_form,
                'profile_form': profile_form
            }
            return shortcuts.render(request, self.template_name, context)


class UserChangePasswordView(PermissionRequiredMixin, FormView):
    raise_exception = True
    model = auth_models.User
    form_class = auth_forms.SetPasswordForm
    template_name = 'user_change_password_view.html'

    def get_form(self, form_class=None):
        self.user = shortcuts.get_object_or_404(auth_models.User, pk=self.kwargs['pk'])
        if form_class is None:
            form_class = self.get_form_class()
        return form_class(self.user, **self.get_form_kwargs())

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return shortcuts.reverse('users:user_detail', args=[self.user.id])

    def has_permission(self):
        return self.request.user.is_authenticated and (
            self.request.user.is_superuser or self.request.user.id == int(self.kwargs['pk']))


class UserDeleteView(LoginSuperuserRequiredMixin, DeleteView):
    raise_exception = True
    model = auth_models.User
    template_name = 'user_delete_view.html'
    success_url = reverse_lazy('users:user_list')
