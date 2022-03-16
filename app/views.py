from django.http import HttpResponse
from rest_framework import generics
from multiprocessing import AuthenticationError
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout

from .serializers import *
from .models import *
from .forms import *

# def add_bron_db(audDate):
#     brons = Bron.objects.filter(date=audDate.date)
#     for bron in brons:
#         print(bron)
        # audDate.hour0 = bool(bron.hour0 + audDate.hour0)
        # audDate.hour0 = bool(bron.hour0 + audDate.hour0)
        # audDate.hour0 = bool(bron.hour0 + audDate.hour0)
        # audDate.hour0 = bool(bron.hour0 + audDate.hour0)
        # audDate.hour0 = bool(bron.hour0 + audDate.hour0)
        # audDate.hour0 = bool(bron.hour0 + audDate.hour0)
        # audDate.hour0 = bool(bron.hour0 + audDate.hour0)
        # audDate.hour0 = bool(bron.hour0 + audDate.hour0)
        # audDate.hour0 = bool(bron.hour0 + audDate.hour0)
        # audDate.hour0 = bool(bron.hour0 + audDate.hour0)
        # audDate.save()



def bron(request, year=None, month=None, day=None):
    auditors = Auditor.objects.all()
    if request.POST:
        post = request.POST
        print(post)
        type_post = post.get('type')
        if type_post == 'search_date':
            date = post.get('date').split('-')
            # req = [post.get('places')]
            # req.append(post.get('tables'))
            # req.append(post.get('computers'))
            # req.append(post.get('interactive'))
            # req.append(post.get('proektor'))
            # req.append(post.get('micro'))
            # req.append(post.get('speakers'))
            # req.append(post.get('corpus'))

            redir = ''
            if post.get('places') != None:
                redir += 'places'+'='+post.get('places')+'&'
            if post.get('tables') != None:
                redir += 'tables'+'='+post.get('tables')+'&'
            if post.get('computers') != None:
                redir += 'computers'+'='+post.get('computers')+'&'
            if post.get('interactive') != None:
                redir += 'interactive'+'='+'1'+'&'
            if post.get('proektor') != None:
                redir += 'proektor'+'='+'1'+'&'
            if post.get('micro') != None:
                redir += 'microphones'+'='+'1'+'&'
            if post.get('speakers') != None:
                redir += 'speakers'+'='+'1'+'&'
            if post.get('corpus'):
                redir += 'corpus'+'='+post.get('corpus')
            return redirect('/day/'+ date[0]+ '/'+ date[1]+ '/'+ date[2]+
            '?'+redir)

        elif type_post == 'send':
            form = BronForm(post)
            if form.is_valid():
                form.save()
                aud = Auditor.objects.last()
                aud.user = post.get('user')
                aud.save()
        else:
            form = BronForm(post)
            if form.is_valid():
                form.save()
                aud = Auditor.objects.last()
                aud.user = post.get('user')
                aud.save()
    elif request.GET:
        get = request.GET
        req = [False for i in range(8)]
        req[0] = get.get('places')
        req[1] = get.get('tables')
        req[2] = get.get('computers')
        req[3] = get.get('interactive')
        req[4] = get.get('proektor')
        req[5] = get.get('micro')
        req[6] = get.get('speakers')
        req[7] = get.get('corpus')
        for r in range(len(req)):
            if req[r] == None:
                req[r] = False
            elif req[r] == 'on':
                req[r] = True
                
        
        if req[7] and req[7] != '0':
            auditors = Auditor.objects.filter(places__gte=req[0],
            tables__gte=req[1], computers__gte=req[2],
            interactiveBoard__gte=req[3], proektor__gte=req[4], microphones__gte=req[5], 
            speakers__gte=req[6], corpus=req[7])
        else:
            auditors = Auditor.objects.filter(places__gte=req[0],
            tables__gte=req[1], computers__gte=req[2],
            interactiveBoard__gte=req[3], proektor__gte=req[4], microphones__gte=req[5], 
            speakers__gte=req[6])

    else:
        auditors = Auditor.objects.all()



        
    
    
    # add_bron_db(AuditorDate.objects.get(pk=1))

    if year and month and day:
        date=str(year)+'-'+str(month)+'-'+str(day)
        
    else:
        date=None
    
    # for br in Bron.objects.filter(date=date)
    
    context = {
        'auditors': auditors,
        'form': BronForm,
        'user': request.user,
        'date': date,
        'bron': Bron.objects.filter(date=date, allowed=True),
        'corpusies': Corpus.objects.all(),
        'count': auditors.count()
    }
    return render(request, 'app/index.html', context)

def auditors(request):
    auditors = Auditor.objects.all()
    context = {
        'auditors': auditors,
    }
    return render(request, 'app/auditors.html', context)

def logout_user(request):
    logout(request)
    return redirect('/')

# def auditorDate(request, year, month, day):
#     date=str(year)+'-'+str(month)+'-'+str(day)
#     auditorsdate = AuditorDate.objects.all().filter(date=date)
#     auditors = Auditor.objects.all()
#     setaud = set()
#     for aud in auditorsdate:
#         setaud.add(aud.auditor.pk)
#     for aud in auditors:
#         if aud.pk not in setaud:
#             AuditorDate.objects.create(date=date, auditor=aud)
#     context = {
#         'auditors': AuditorDate.objects.all().filter(date=date),
#     }
#     return render(request, 'app/auditors_date.html', context)

class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'app/login.html'
    

class AuditorAPI(generics.ListAPIView):
    
    queryset = Auditor.objects.all()
    serializer_class = AuditorSerializer


class BronAPI(generics.ListAPIView):
    
    queryset = Bron.objects.all()
    serializer_class = BronSerializer

