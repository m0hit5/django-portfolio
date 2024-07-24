# p_app/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail
from .models import Project, Contact
from .forms import ContactForm
from django.conf import settings

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def projects(request):
    projects = Project.objects.all()
    return render(request, 'projects.html', {'projects': projects})

def project_detail(request, id):
    project = get_object_or_404(Project, id=id)
    return render(request, 'project_detail.html', {'project': project})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            # Prepare email content
            subject = 'New Contact Form Submission'
            message = f"Name: {form.cleaned_data['name']}\nEmail: {form.cleaned_data['email']}\nMessage: {form.cleaned_data['message']}"
            from_email = settings.DEFAULT_FROM_EMAIL
            recipient_list = ['to@example.com']  # Replace with your email

            # Send email
            send_mail(subject, message, from_email, recipient_list, fail_silently=False)
            return render(request, 'contact.html', {'form': form, 'success': True})
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})
