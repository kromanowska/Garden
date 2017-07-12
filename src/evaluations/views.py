from django_datatables_view.base_datatable_view import BaseDatatableView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, TemplateView
from django.contrib.auth import models as auth_models
from django.template import defaultfilters
from django import shortcuts
from django.urls import reverse_lazy
from django.db.models import Q
from common.mixins import LoginDifferentSuperuserRequiredMixin, LoginSuperuserRequiredMixin
from evaluations import models as evaluation_models
from evaluations import forms


class EvaluationListView(LoginSuperuserRequiredMixin, TemplateView):
    template_name = 'evaluation_list_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = forms.EvaluationSearchForm()
        return context


class EvaluationDataTableView(PermissionRequiredMixin, BaseDatatableView):
    raise_exception = True
    model = evaluation_models.Evaluation
    columns = ['user__last_name', 'user__profile__department',
               'summary_evaluation', 'submited_by', 'submited', 'urls']
    order_columns = ['user__last_name', 'user__profile__department',
                     'summary_evaluation', 'submited_by', 'submited', 'urls']
    max_display_length = 20

    def get_initial_queryset(self):
        return super().get_initial_queryset() \
            .select_related('user', 'user__profile', 'user__profile__department', 'submited_by')

    def render_column(self, row, column):
        if column == 'user__last_name':
            return row.user.get_full_name()
        elif column == 'user__profile__department':
            return row.user.profile.department.name
        elif column == 'summary_evaluation':
            return evaluation_models.Evaluation.get_evaluation_label(row.summary_evaluation)
        elif column == 'submited_by':
            return row.submited_by.get_full_name()
        elif column == 'submited':
            return defaultfilters.date(row.submited, 'DATE_FORMAT')
        elif column == 'urls':
            urls = {}
            if self.request.user.is_superuser or self.request.user.id == row.user.id:
                urls['detail_url'] = shortcuts.reverse('evaluations:evaluation_detail', args=[row.id])
            if self.request.user.is_superuser and self.request.user.id != row.user.id:
                urls['update_url'] = shortcuts.reverse('evaluations:evaluation_update', args=[row.id]),
                urls['delete_url'] = shortcuts.reverse('evaluations:evaluation_delete', args=[row.id])
            return urls
        else:
            return super().render_column(row, column)

    def filter_queryset(self, qs):
        qset = Q()

        name = self.request.POST.get('name')
        if name:
            qset &= (Q(user__first_name__istartswith=name)
                     | Q(user__last_name__istartswith=name))

        submited_from = self.request.POST.get('submited_from')
        if submited_from:
            qset &= Q(submited__gte=submited_from)

        submited_to = self.request.POST.get('submited_to')
        if submited_to:
            qset &= Q(submited__lte=submited_to)

        department = self.request.POST.get('department')
        if department:
            qset &= Q(user__profile__department_id=department)

        return qs.filter(qset)

    def has_permission(self):
        return self.request.user.is_superuser


class EvaluationUserDataTableView(EvaluationDataTableView):
    columns = ['summary_evaluation', 'submited_by', 'submited', 'urls']
    order_columns = ['summary_evaluation', 'submited_by', 'submited', 'urls']

    def get_initial_queryset(self):
        return super().get_initial_queryset() \
            .filter(user_id=self.kwargs['pk']) \
            .select_related('user', 'user__profile', 'user__profile__department', 'submited_by')

    def has_permission(self):
        return self.request.user.is_superuser or self.request.user.id == int(self.kwargs['pk'])


class EvaluationDetailView(PermissionRequiredMixin, DetailView):
    raise_exception = True
    model = evaluation_models.Evaluation
    template_name = 'evaluation_detail_view.html'

    def has_permission(self):
        evaluation = self.get_object()
        return self.request.user.is_authenticated and (
            self.request.user.is_superuser or self.request.user.id == evaluation.user.id)


class EvaluationCreateView(LoginDifferentSuperuserRequiredMixin, CreateView):
    raise_exception = True
    model = evaluation_models.Evaluation
    fields = [
        'knowledge', 'quality', 'quantity', 'task_and_project_management', 'dependability',
        'adaptability_stress_tolerance', 'initiative_resourcefullness', 'judgment_decision_making',
        'relationships_with_people_and_communication', 'departmental_policies_and_procedures',
        'employee_development_and_goal_setting', 'improvement_plan_employee', 'improvement_plan_supervisor',
        'supervisor_recommendation'
    ]
    template_name = 'evaluation_create_view.html'
    success_url = reverse_lazy('evaluations:evaluation_detail')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = shortcuts.get_object_or_404(auth_models.User, pk=self.kwargs['pk'])
        return context

    def form_valid(self, form):
        form.instance.user = shortcuts.get_object_or_404(auth_models.User, pk=self.kwargs['pk'])
        form.instance.submited_by = self.request.user
        form.instance.compute_summary_points()
        form.instance.compute_summary_evaluation()
        return super().form_valid(form)

    def get_success_url(self):
        return shortcuts.reverse('evaluations:evaluation_detail', args=[self.object.id])


class EvaluationUpdateView(LoginDifferentSuperuserRequiredMixin, UpdateView):
    raise_exception = True
    model = evaluation_models.Evaluation
    fields = [
        'knowledge', 'quality', 'quantity', 'task_and_project_management', 'dependability',
        'adaptability_stress_tolerance', 'initiative_resourcefullness', 'judgment_decision_making',
        'relationships_with_people_and_communication', 'departmental_policies_and_procedures',
        'employee_development_and_goal_setting', 'improvement_plan_employee', 'improvement_plan_supervisor',
        'supervisor_recommendation'
    ]
    template_name = 'evaluation_update_view.html'
    success_url = reverse_lazy('evaluations:evaluation_detail')

    def form_valid(self, form):
        form.instance.submited_by = self.request.user
        form.instance.compute_summary_points()
        form.instance.compute_summary_evaluation()
        return super().form_valid(form)

    def get_success_url(self):
        return shortcuts.reverse('evaluations:evaluation_detail', args=[self.object.id])


class EvaluationDeleteView(LoginDifferentSuperuserRequiredMixin, DeleteView):
    raise_exception = True
    model = evaluation_models.Evaluation
    template_name = 'evaluation_delete_view.html'
    success_url = reverse_lazy('evaluations:evaluation_list')
