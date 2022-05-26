from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from sympy import *
from sympy.printing.latex import latex
import random
from calc_probs.indef_integral_checker import checker

from .models import IntegralQuestion

def index(request):
    integral_question_list = IntegralQuestion.objects.order_by('id')
    random_id = random.choice(IntegralQuestion.objects.values_list('id', flat=True))
    context = {
        'integral_question_list': integral_question_list,
        'random_id': random_id,
        }
    return render(request, 'calc_probs/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(IntegralQuestion, pk=question_id)
    return render(request, 'calc_probs/detail.html',
                  {'question': question,
                   })

def result(request, question_id):
    question = get_object_or_404(IntegralQuestion, pk=question_id)
    user_answer = request.POST.get('user_answer')
    try:
        x = Symbol('x')
        latex_previous = latex(eval(user_answer))
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
                random_id = random.choice(IntegralQuestion.objects.values_list('id', flat=True))
                return render(request, 'calc_probs/detail.html',
                    {'question': question,
                    'correct': True,
                    'previous_input': request.POST.get('user_answer'),
                    'latex_previous': latex_previous,
                    'random_id': random_id,
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
        latex_result_true = latex(Integral(eval(prev_grand_input), x)) + ' = ' + latex(eval(prev_ii_input)) + ' + C'
        latex_result_false = latex(Integral(eval(prev_grand_input), x)) + r' \not= ' +latex(eval(prev_ii_input)) + ' + C'
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

    