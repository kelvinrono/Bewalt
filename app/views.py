from django.shortcuts import render,redirect

from .models import Gallery
from .forms import ClientForm

from django.contrib import messages
from .email import send_welcome_email,send_director_email


def home(request):
    return render(request, 'index.html')

def email(request):
    if request.method == 'POST':
        form=ClientForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']

            # recipient = ClientForm(name = name,email =email)
            # recipient.save()
            request = form.save(commit=False)
            name = request.name
            email = request.email
            admin_name='Director'
           
            send_welcome_email(name,email)
            send_director_email(admin_name)
                 

            request.save()
            # messages.success(request, f'Your request has been received. Check your Email!')

            return redirect('home')
    else:
        # messages.warning(request, f'Data was not inserted')
        form=ClientForm()
    params={
        'form':form
    }

    return render(request, 'index.html',params)


def projects(request):
    
    projects=Gallery.objects.all()

    context={
        'projects':projects
    }
    return render(request, 'projects.html', context)