from django.shortcuts import render, redirect, get_list_or_404
from django.views.generic import View 
from django.http import HttpResponse 
# Create your views here.

class TestView(View):
    def get(self, request):
        return HttpResponse('<h1>Test</h1>')

class TestTplView(View):
    def get(self, request):
        template = 'member/index.html'
        data = {
            'kata':'test view blblbllb',
            'array': [1,2,3,4,5],
            'logika': True,
        }
        return render(request, template, data)


