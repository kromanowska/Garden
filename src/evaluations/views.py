from django import shortcuts
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import models as auth_models
from evaluations import models as evaluation_models
from common.mixins import LoginDifferentSuperuserRequiredMixin


class EvaluationCreateView(LoginDifferentSuperuserRequiredMixin, CreateView):
    raise_exception = True
    model = evaluation_models.Evaluation
    fields = [
        'knowledge', 'quality', 'quantity', 'task_and_project_management', 'dependability',
        'adaptability_stress_tolerance', 'initiative_resourcefullness', 'judgment_decision_making',
        'relationships_with_people_and_communication', 'departmental_college_policies_and_procedures',
        'employee_development_and_goal_setting', 'improvement_plan_employee', 'improvement_plan_supervisor',
        'supervisor_recommendation'
    ]
    template_name = 'evaluation_create_view.html'
    success_url = reverse_lazy('evaluations:evaluation_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = shortcuts.get_object_or_404(auth_models.User, pk=self.kwargs['pk'])
        return context

    def form_valid(self, form):
        form.instance.user = shortcuts.get_object_or_404(auth_models.User, pk=self.kwargs['pk'])
        form.instance.submited_by = self.request.user
        form.instance.summary_points = self._get_summary_points(form)
        form.instance.summary_evaluations = self._get_summary_evaluations(form.instance.summary_points)
        return super().form_valid(form)

    def _get_summary_points(self, form):
        return form.instance.knowledge + \
               form.instance.quality + \
               form.instance.quantity + \
               form.instance.task_and_project_management + \
               form.instance.dependability + \
               form.instance.adaptability_stress_tolerance + \
               form.instance.initiative_resourcefullness + \
               form.instance.judgment_decision_making + \
               form.instance.relationships_with_people_and_communication + \
               form.instance.departmental_college_policies_and_procedures + \
               form.instance.employee_development_and_goal_setting

    def _get_summary_evaluations(self, summary_points):
        return round(summary_points / 11)
