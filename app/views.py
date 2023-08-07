from django.shortcuts import render
from django.http import HttpResponse
from app.forms import *
from django.views.generic import View, TemplateView

## Create your views here.

class data_rendering(View):
    def get(self, request):
        d = {'name':'Tushar'}
        return render(request, 'data_render.html',d)




## Fbv_insert

def fbv_insert(request):
    SFO = StudentForm()
    d={'SFO':SFO}
    if request.method=='POST':
        SFD=StudentForm(request.POST)
        if SFD.is_valid():
            SFD.save()
            return HttpResponse('Data inserted')
    return render(request,'insert_fbv.html',d)


## Cbv_insert
class Cbv_insert(View):
    def get(self,request):
        SFO=StudentForm()
        d={'SFO':SFO}
        return render(request,'Cbv_insert.html',d)
    def post(self,request):
        SFD=StudentForm(request.POST)
        if SFD.is_valid():
            SFD.save()
            return HttpResponse('Cbv_insert')

