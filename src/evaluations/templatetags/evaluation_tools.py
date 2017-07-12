from django import template
from evaluations import models

register = template.Library()


@register.filter
def evaluation_label(value):
    return models.Evaluation.get_evaluation_label(value)
