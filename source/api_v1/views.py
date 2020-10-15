from django.shortcuts import render

import json
from datetime import datetime
from django.http import HttpResponse, HttpResponseNotAllowed, JsonResponse, HttpResponseNotFound
from django.views.decorators.csrf import ensure_csrf_cookie

@ensure_csrf_cookie
def get_token_view(request, *args, **kwargs):
    if request.method == 'GET':
        return HttpResponse()
    return HttpResponseNotAllowed("Only GET method")


def json_echo_view(request, *args, **kwargs):
    answer = {
        'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'method': request.method,
    }
    if request.method == 'POST':
        data = json.loads(request.body)
        answer['data'] = data
    return JsonResponse(answer)


def add_view(request, *args, **kwargs):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            a = data['A']
            b = data['B']
            result = int(a) + int(b)
            answer = {
                'answer': result
            }
            return JsonResponse(answer)
        except:
            response = JsonResponse({'error': 'No data provided!'})
            response.status_code = 400
            return response


def subtract_view(request, *args, **kwargs):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            a = data['A']
            b = data['B']
            result = int(a) -int(b)
            answer = {
                'answer': result
            }
            return JsonResponse(answer)
        except:
            response = JsonResponse({'error': 'No data provided!'})
            response.status_code = 400
            return response


def multiply_view(request, *args, **kwargs):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            a = data['A']
            b = data['B']
            result = int(a) * int(b)
            answer = {
                'answer': result
            }
            return JsonResponse(answer)
        except:
            response = JsonResponse({'error': 'No data provided!'})
            response.status_code = 400
            return response


def divide_view(request, *args, **kwargs):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            a = data['A']
            b = data['B']
            result = int(a) / int(b)
            answer = {
                'answer': result
            }
            return JsonResponse(answer)
        except:
            response = JsonResponse({'error': 'No data provided!'})
            response.status_code = 400
            return response


def main_view(request, *args, **kwargs):
    if request.method == 'GET':
        return render(request,'index.html')
    else:
        return HttpResponseNotFound
