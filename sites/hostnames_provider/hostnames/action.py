from hostnames.model import Host

def contact(request):
    if request.method == 'POST': # If the form has been submitted...
        form = ContactForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...

            hostnameF =  form.cleaned_data['hostname']
            ipaddF = form.cleaned_data['ipadd']
            macaddF = form.cleaned_data['macadd']

            print form.cleaned_data['hostname']
            
            q = Host(hostname=hostnameF,ip_adress=ipaddF,mac_adress=macaddF)
            #q.save()
    else:
        form = ContactForm() # An unbound form
    })
