from django.http import HttpResponse
from django.shortcuts import render
from AppProyectoWeb.forms import ContactoForm
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def home(request):
    
    return render (request,'home.html')



def tienda(request):
    
    return render (request,'tienda.html')



def contacto(request):
    
    if request.method == 'POST':
        
        miFormularioContacto = ContactoForm(request.POST)
        
        if miFormularioContacto.is_valid():
            
            infoForm=miFormularioContacto.cleaned_data
            
            send_mail(infoForm['asunto'],infoForm['mensaje'],
                      infoForm.get('email',settings.EMAIL_HOST_USER),['gusgeneris92@gmail.com'])

            return render (request,'home.html')
        
    else:
        miFormularioContacto=ContactoForm()
    
    return render (request,'contacto.html',{'formulario':miFormularioContacto})




