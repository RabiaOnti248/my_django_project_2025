from django.shortcuts import render, redirect
from .models import ContactMessage # ContactMessage model import

# Home Page View
def home_view(request):
    return render(request, 'basicapp/home.html')

# About Us Page View
def about_view(request):
    return render(request, 'basicapp/about.html')

# Contact Page View (with form handle)
def contact_view(request):
    submitted = False
    
    # confirm form submit (POST request)
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        # database inform saved
        ContactMessage.objects.create(
            name=name, 
            email=email, 
            message=message
        )
        
        #successfully submit form redirection page refresh
        return redirect('/contact/?submitted=True') 
        
    # IF GET request / 
    if 'submitted' in request.GET:
        submitted = True # If URL submitted=True 
        
    return render(request, 'basicapp/contact.html', {'submitted': submitted})