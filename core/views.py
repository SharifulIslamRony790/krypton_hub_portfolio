from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ContactMessage

def home_view(request):
    """
    Renders the main landing page and handles the contact form submission.
    """
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        company = request.POST.get('company')
        phone = request.POST.get('phone')
        service = request.POST.get('service')
        message = request.POST.get('message')
        
        # Server-side validation
        if not name or not email or not message:
            messages.error(request, 'Please fill in all required fields.')
            return redirect('home')
            
        try:
            ContactMessage.objects.create(
                name=name,
                email=email,
                company=company,
                phone=phone,
                service=service,
                message=message
            )
            messages.success(request, 'Thank you! Your message has been sent successfully. We will get back to you soon.')
        except Exception as e:
            messages.error(request, 'An error occurred while sending your message. Please try again later.')
            
        return redirect('home')
        
    return render(request, 'core/home.html')
