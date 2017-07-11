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
    submited = models.DateField(auto_now_add=True)

    knowledge = models.IntegerField(choices=POINTS_CHOICES, default=DEFAULT_POINT_CHOICE)
    quality = models.IntegerField(choices=POINTS_CHOICES, default=DEFAULT_POINT_CHOICE)
    quantity = models.IntegerField(choices=POINTS_CHOICES, default=DEFAULT_POINT_CHOICE)
    task_and_project_management = models.IntegerField(choices=POINTS_CHOICES, default=DEFAULT_POINT_CHOICE)
    dependability = models.IntegerField(choices=POINTS_CHOICES, default=DEFAULT_POINT_CHOICE)
    adaptability_stress_tolerance = models.IntegerField(choices=POINTS_CHOICES, default=DEFAULT_POINT_CHOICE)
    initiative_resourcefullness = models.IntegerField(choices=POINTS_CHOICES, default=DEFAULT_POINT_CHOICE)
    judgment_decision_making = models.IntegerField(choices=POINTS_CHOICES, default=DEFAULT_POINT_CHOICE)
    relationships_with_people_and_communication = models.IntegerField(
        choices=POINTS_CHOICES, default=DEFAULT_POINT_CHOICE)
    departmental_college_policies_and_procedures = models.IntegerField(
        choices=POINTS_CHOICES, default=DEFAULT_POINT_CHOICE)
    employee_development_and_goal_setting = models.IntegerField(choices=POINTS_CHOICES, default=DEFAULT_POINT_CHOICE)

    summary_points = models.IntegerField()
    summary_evaluations = models.IntegerField(choices=POINTS_CHOICES)

    improvement_plan_employee = models.TextField()
    improvement_plan_supervisor = models.TextField()
    supervisor_recommendation = models.TextField()
