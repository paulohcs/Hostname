from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.template import loader, RequestContext
from django.template.context_processors import csrf
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response


from .models import Host
from .forms import *

# Create your views here.

def hostname(request):
    if request.method == 'GET':
        form = HostForm(request.GET)
        if form.is_valid():
            mac = form.cleaned_data['mac']
            ip = form.cleaned_data['ip']
            h = Host.objects.get(ip_address=ip, mac_address=mac)
            return HttpResponse(h.hostname)
        else:
            return HttpResponse(form)

def hostnameCreate(request):
    c = {}
    c.update(csrf(request))
    if request.method == 'POST':
        form = CreateForm(request.POST)
        if form.is_valid():
            hostForm = form.cleaned_data['hostname']
            macForm = form.cleaned_data['mac']
            ipForm = form.cleaned_data['ip']
            h = Host(hostname=hostForm,mac_address=macForm,ip_address=ipForm)
            h.save()
            return HttpResponseRedirect("/list")
        else:
            return HttpResponseRedirect("/list")

def hostnameUpdate(request):
    c = {}
    c.update(csrf(request))
    if request.method == 'POST':
        form = EditForm(request.POST)
        if form.is_valid():
            h = Host.objects.get(id=form.cleaned_data['id'])
            h.hostname = form.cleaned_data['hostname']
            h.mac_address = form.cleaned_data['mac']
            h.ip_address = form.cleaned_data['ip']
            h.save()
            return HttpResponseRedirect("/list")
        else:
            return HttpResponseRedirect("/list")

def delete(request):
    c = {}
    c.update(csrf(request))
    if request.method == 'POST':
        form = DeleteForm2(request.POST)
        if form.is_valid():
            h = Host.objects.get(id=form.cleaned_data['id'])
            h.delete()
            return HttpResponseRedirect("/list")
        else:
            return HttpResponseRedirect("/list")

def index(request):
    ip = request.META['REMOTE_ADDR']
    h = Host.objects.get(ip_address='200.131.179.255')
    return HttpResponse(h.hostname)

def create(request):
    if (request.method == 'GET'): # redirecionamento padrao
        template = loader.get_template('hostnames/create.html')
        c = RequestContext (request, {})
        return HttpResponse(template.render(c))
    if (request.method == 'POST'): #
        c = {}
        c.update(csrf(request))
        form = CreateForm(request.POST)
        if form.is_valid():
            hostForm = form.cleaned_data['hostname']
            macForm = form.cleaned_data['mac']
            ipForm = form.cleaned_data['ip']
            h = Host(hostname=hostForm,mac_address=macForm,ip_address=ipForm)
            h.save()
            return HttpResponseRedirect("/list")
        else:
            return HttpResponseRedirect("/list")
        

def update(request):
    if (request.method == 'GET'): # redirecionamento padrao
        ip = request.GET['ip']
        template = loader.get_template('hostnames/update.html')
        c = RequestContext(request, {
            'host' : Host.objects.get(ip_address=ip),
        })
        return HttpResponse(template.render(c))
    if (request.method == 'POST'): #
        c = {}
        c.update(csrf(request))
        form = EditForm(request.POST)
        if form.is_valid():
            h = Host.objects.get(id=form.cleaned_data['id'])
            h.hostname = form.cleaned_data['hostname']
            h.mac_address = form.cleaned_data['mac']
            h.ip_address = form.cleaned_data['ip']
            h.save()
            return HttpResponseRedirect("/list")
        else:
            return HttpResponseRedirect("/list")

def retrieve(request):
    ip = request.GET['ip']
    template = loader.get_template('hostnames/retrieve.html')
    c = RequestContext(request, {
        'host' : Host.objects.get(ip_address=ip),
    })
    return HttpResponse(template.render(c))

def list(request):
    template = loader.get_template('hostnames/list.html')
    c = RequestContext(request, {
        'hosts' : Host.objects.all(),
    })
    return HttpResponse(template.render(c))

def insert_host(request):
    if request.method == 'GET': # If the form has been submitted...
        form = CreateForm(request.GET) # A form bound to the GET data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...

            hostnameF =  form.cleaned_data['hostname']
            ipaddF = form.cleaned_data['ip']
            macaddF = form.cleaned_data['mac']
    
            print form.cleaned_data['hostname']
            
            h = Host(hostname=hostnameF,ip_address=ipaddF,mac_address=macaddF)
            h.save()
            return HttpResponseRedirect("/list")
        else:
            form = ContactForm() # An unbound form
