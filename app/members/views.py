from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from members.models import Member

def members(request):
    lista = Member.objects.all().values()
    template = loader.get_template('all_members.html')
    context = {
        'mymembers': lista
    }
    return HttpResponse(template.render(context, request))
    #template = loader.get_template('myfirst.html')
    #return HttpResponse(template.render())
    # return HttpResponse("Olá Mundo!")

def details(request, id):
    mymember = Member.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'mymember': mymember
    }
    return HttpResponse(template.render(context, request))

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())