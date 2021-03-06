from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import generic
from django_filters.views import FilterView
from calc_probs.filters import QuestionFilter
from sympy import *
from sympy.printing.latex import latex
import random
from calc_probs.indef_integral_checker import checker

from .models import IntegralQuestion

class IndexView(FilterView):
    template_name = 'calc_probs/index.html'
    model = IntegralQuestion
    context_object_name = 'integral_question_list'
    filterset_class = QuestionFilter

    def get_queryset(self):
        """Return all the integral questions ordered by id."""
        return IntegralQuestion.objects.order_by('id')

class DetailView(generic.DetailView):
    model = IntegralQuestion
    template_name = 'calc_probs/detail.html'
    context_object_name = 'question'

def random_prob(request):
    random_id = random.choice(IntegralQuestion.objects.values_list('id', flat=True))
    question = get_object_or_404(IntegralQuestion, pk=random_id)
    return render(request, 'calc_probs/detail.html',
                {'question': question,
                })

def result(request, question_id):
    question = get_object_or_404(IntegralQuestion, pk=question_id)
    user_answer = request.POST.get('user_answer')
    try:
        x = Symbol('x')
        latex_previous = latex(parsing.sympy_parser.parse_expr(user_answer))
        correct = checker(question.integrand, user_answer)
        if 'preview' in request.POST:
            return render(request, 'calc_probs/detail.html',
                {'question': question,
                'preview': True,
                'previous_input': request.POST.get('user_answer'),
                'latex_previous': latex_previous,
                })
        elif 'submit' in request.POST:
            if correct:
                return render(request, 'calc_probs/detail.html',
                    {'question': question,
                    'correct': True,
                    'previous_input': request.POST.get('user_answer'),
                    'latex_previous': latex_previous,
                    })
            if not correct:
                return render(request, 'calc_probs/detail.html',
                    {'question': question,
                    'incorrect': True,
                    'previous_input': request.POST.get('user_answer'),
                    'latex_previous': latex_previous,
                    })
    except:
        return render(request, 'calc_probs/detail.html',
                {'question': question,
                'error_message': 'Invalid input!',
                'previous_input': request.POST.get('user_answer'),
                })

def check(request):
    return render(request, 'calc_probs/check.html')

def check_result(request):
    prev_grand_input = request.POST.get('grand_input')
    prev_ii_input = request.POST.get('ii_input')
    x = Symbol('x')
    try:
        latex_result_true = latex(Integral(parsing.sympy_parser.parse_expr(prev_grand_input), x)) + ' = ' + latex(parsing.sympy_parser.parse_expr(prev_ii_input)) + ' + C'
        latex_result_false = latex(Integral(parsing.sympy_parser.parse_expr(prev_grand_input), x)) + r' \not= ' +latex(parsing.sympy_parser.parse_expr(prev_ii_input)) + ' + C'
        correct = checker(prev_grand_input, prev_ii_input)
        if correct:
            return render(request, 'calc_probs/check.html',
                    {'correct': True,
                    'latex_result': latex_result_true,
                    'prev_grand_input': prev_grand_input,
                    'prev_ii_input': prev_ii_input,
                    })
        else:
            return render(request, 'calc_probs/check.html',
                    {'latex_result': latex_result_false,
                    'prev_grand_input': prev_grand_input,
                    'prev_ii_input': prev_ii_input,
                    })
    except:
        return render(request, 'calc_probs/check.html',
                    {'prev_grand_input': prev_grand_input,
                    'prev_ii_input': prev_ii_input,
                    'error_message': 'Invalid input!'
                    })