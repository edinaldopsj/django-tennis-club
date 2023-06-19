from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# from heroes.models import Hero
# Create your views here.
def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

def heroes(request):
    # lista = Member.objects.all().values()
    template = loader.get_template('all_heroes.html')
    context = {
        'myheroes': '' # lista
    }
    return HttpResponse(template.render(context, request))

def new_hero(request):
    template = loader.get_template('new_hero.html')
    return HttpResponse(template.render())\
    
# def addhero(request):
#     nome = request.POST['nome']
#     rs = request.POST['rs']
#     ph = request.POST['phone']

#     fabri = Fabricante(name=nome, razao_social=rs, phone=ph,joined_date=datetime.date.today())

#     fabri.save()
#     return HttpResponseRedirect(reverse('fabricantes'))