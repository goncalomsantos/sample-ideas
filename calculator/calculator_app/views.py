from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect
import ast

# Create your views here.
def calculator(request):
    return render(request, 'calculator_app/calculator.html')

@csrf_protect
def calculate(request):
    if request.method == 'POST':
        try:
            expression = request.POST.get('expression', '')
            result = eval(expression)

            return JsonResponse({'result': result})
        except Exception as e:
            return JsonResponse({'error': f'Error during calculation: {str(e)}'})
    else:
        return JsonResponse({'error': 'Invalid request method.'})
