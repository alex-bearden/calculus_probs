import django_filters
from .models import IntegralQuestion

class QuestionFilter(django_filters.FilterSet):
    class Meta:
        model = IntegralQuestion
        fields = ['technique']