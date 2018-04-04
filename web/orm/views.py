from django.shortcuts import render, redirect
from django.contrib.auth.mixin import LoginRequiredMixin
from django.http import HttpResponse 
from django.views.generic import View    
from orm.models import Orm 
from orm.forms import OrmForm
from library.views import AdminAccessView
# Create your views here.

class OrmList(AdminAccessView):
    def get(self, request):
        templateName = 'orm/list.html'
        data = {
            'orms': Orm.objects.all(),
        }
        return render(request, templateName, data)

class OrmAdd(AdminAccessView):
    def get(self, request):
        templateName = 'orm/add.html'
        data = [
            'form' : form,
            'mode' : 'add',
        ]
        return render(request, templateName, data)

class OrmSave(AdminAccessView):
    def post(self, request):
        templateName = 'orm/add.html'
        form = OrmForm(request.POST or None)
        if form.is_valid():
            b = Orm()
            b.nama = form.cleaned_data['nama']
            b.luas = form.cleaned_data['luas']
            b.kapasitas = form.cleaned_data['kapasitas']
            b.member = form.cleaned_data['member']
            b.save()
        else:
            data = {
                'form': form,  
            }
            return render(request, templateName, data)
        return redirect('orm:list')

class OrmEdit(AdminAccessView):
    def get(self, request, pk):
        templateName = 'orm/edit.html'
        b = Orm.objects.get(pk=pk)
        orm_init ={
            'nama': b.nama,
            'luas': b.luas,
            'kapasitas': b.kapasitas,
            'member' :b.member,
        }
        form = OrmForm(request.POST or None, initial=orm_init)
        data = {
            'orm' : form, 
            'id' : pk, 
        }
        return render(request, templateName, data)

class OrmUpdate(AdminAccessView):
    def post (self, request, pk):
        templateName = 'orm/edit.html'
        form = OrmForm(request.POST or None)
        if form.is_valid():
            b = Orm.objects.get(pk=pk)
            b.nama = form.cleaned_data['nama']
            b.luas = form.cleaned_data['luas']
            b.kapasitas = form.cleaned_data['kapasitas']
            b.member = form.cleaned_data['member']
            b.save(force_update=True)
        else:
            data = {
                'form' : form,
                'id': pk, 
            }
        return redirect('room:list')

class OrmDelete(AdminAccessView):
    def get(self, request, pk):
        b = Room.objects.get(pk=pk)
        b.delete()
        return redirect('room:list')