from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from heroes.models import Hero

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

def heroes(request):
    myheroes = Hero.objects.all()
    template = loader.get_template('all_heroes.html')
    context = {
        'myheroes': myheroes
    }
    return HttpResponse(template.render(context, request))

def new_hero(request):
    template = loader.get_template('new_hero.html')
    return HttpResponse(template.render())

def add_hero(request):
    name = request.POST['name']
    str = request.POST['str']
    dex = request.POST['dex']
    con = request.POST['con']
    int = request.POST['int']
    wis = request.POST['wis']
    cha = request.POST['cha']

    hero = Hero(name=name, str=str, dex=dex, con=con, int=int, wis=wis, cha=cha)

    hero.save()
    return HttpResponseRedirect(reverse('heroes'))

def update_hero(request, id):
    hero = Hero.objects.get(id=id)
    template = loader.get_template('update_hero.html')
    context = {
        'hero': hero
    }

    return HttpResponse(template.render(context, request))

def update_hero_data(request, id):
    name = request.POST['name']
    str = request.POST['str']
    dex = request.POST['dex']
    con = request.POST['con']
    int = request.POST['int']
    wis = request.POST['wis']
    cha = request.POST['cha']

    hero = Hero.objects.get(id=id)
    hero.name = name
    hero.str = str
    hero.dex = dex
    hero.con = con
    hero.int = int
    hero.wis = wis
    hero.cha = cha

    hero.save()
    return HttpResponseRedirect(reverse('heroes'))

def delete_hero(request, id):
    hero = Hero.objects.get(id=id)
    hero.delete()
    return HttpResponseRedirect(reverse('heroes'))

def hero_detail(request, id):
    hero = Hero.objects.get(id=id)
    template = loader.get_template('hero_detail.html')
    context = {
        'hero': hero
    }
    return HttpResponse(template.render(context, request))