from urllib import request
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from django.views.generic import TemplateView,FormView
from app.forms import *
class Cbv_template(TemplateView):
    template_name='Cbv_template.html'
def mdb(render):
    return render(request,mdb.html)
