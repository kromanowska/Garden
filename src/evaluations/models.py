from django.db import models
from evaluations import enums


class Evaluation(models.Model):
    POINTS_CHOICES = (
        (enums.EmployeeEvaluation.CONSISTENTLY_BELOW_EXPECTATIONS.value, 'Consistently below expectations'),
        (enums.EmployeeEvaluation.BELOW_EXPECTATIONS.value, 'Below expectations'),
        (enums.EmployeeEvaluation.MEETS_EXPECTATIONS.value, 'Meets expectations'),
        (enums.EmployeeEvaluation.EXCEEDS_EXPECTATIONS.value, 'Exceeds expectations'),
        (enums.EmployeeEvaluation.CONSISTENTLY_EXCEEDS_EXPECTATIONS.value, 'Consistently exceeds expectations')
    )
    DEFAULT_POINT_CHOICE = default = enums.EmployeeEvaluation.MEETS_EXPECTATIONS.value

    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='evaluations')
    submited_by = models.ForeignKey('auth.User', related_name='submited_evaluations')
    submited = models.DateField(auto_now=True)

    knowledge = models.IntegerField(choices=POINTS_CHOICES, default=DEFAULT_POINT_CHOICE)
    quality = models.IntegerField(choices=POINTS_CHOICES, default=DEFAULT_POINT_CHOICE)
    quantity = models.IntegerField(choices=POINTS_CHOICES, default=DEFAULT_POINT_CHOICE)
    task_and_project_management = models.IntegerField(choices=POINTS_CHOICES, default=DEFAULT_POINT_CHOICE)
    dependability = models.IntegerField(choices=POINTS_CHOICES, default=DEFAULT_POINT_CHOICE)
    adaptability_stress_tolerance = models.IntegerField(
        choices=POINTS_CHOICES, default=DEFAULT_POINT_CHOICE, verbose_name='Adaptability / stress tolerance')
    initiative_resourcefullness = models.IntegerField(
        choices=POINTS_CHOICES, default=DEFAULT_POINT_CHOICE, verbose_name='Initiative / resourcefullness')
    judgment_decision_making = models.IntegerField(
        choices=POINTS_CHOICES, default=DEFAULT_POINT_CHOICE, verbose_name='Judgment / decision making')
    relationships_with_people_and_communication = models.IntegerField(
        choices=POINTS_CHOICES, default=DEFAULT_POINT_CHOICE)
    departmental_policies_and_procedures = models.IntegerField(
        choices=POINTS_CHOICES, default=DEFAULT_POINT_CHOICE)
    employee_development_and_goal_setting = models.IntegerField(choices=POINTS_CHOICES, default=DEFAULT_POINT_CHOICE)

    summary_points = models.IntegerField(verbose_name='Points')
    summary_evaluation = models.IntegerField(choices=POINTS_CHOICES, verbose_name='Summary')

    improvement_plan_employee = models.TextField()
    improvement_plan_supervisor = models.TextField()
    supervisor_recommendation = models.TextField()

    @property
    def summary_evaluation_label(self):
        return Evaluation.get_evaluation_label(self.summary_evaluation)

    def compute_summary_points(self):
        self.summary_points = self.knowledge + \
                              self.quality + \
                              self.quantity + \
                              self.task_and_project_management + \
                              self.dependability + \
                              self.adaptability_stress_tolerance + \
                              self.initiative_resourcefullness + \
                              self.judgment_decision_making + \
                              self.relationships_with_people_and_communication + \
                              self.departmental_policies_and_procedures + \
                              self.employee_development_and_goal_setting

    def compute_summary_evaluation(self):
        self.summary_evaluation = round(self.summary_points / 11)

    @staticmethod
    def get_evaluation_label(evaluation):
        for value, label in Evaluation.POINTS_CHOICES:
            if value == evaluation:
                return label
        return ''
