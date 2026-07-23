from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
from django.utils.html import escape
from django.core.cache import cache
from django_ratelimit.decorators import ratelimit
from .models import ContactMessage, Service, TeamMember
import re
import requests

@ratelimit(key='ip', rate='5/m', block=False)
def home_view(request):
    """
    Renders the main landing page and handles the contact form submission.
    """
    if getattr(request, 'limited', False):
        messages.error(request, 'You are submitting too many requests. Please try again later.')
        return redirect('home')

    if request.method == 'POST':
        name = escape(request.POST.get('name', ''))
        email = request.POST.get('email', '')
        company = escape(request.POST.get('company', ''))
        phone = request.POST.get('phone', '')
        service_value = request.POST.get('service', '')
        message = escape(request.POST.get('message', ''))

        # Server-side validation
        if not name or not email or not message:
            messages.error(request, 'Please fill in all required fields.')
            return redirect('home')

        # Phone Validation (must start with + and have 7-15 digits)
        if phone:
            if not re.match(r'^\+\d{7,15}$', phone.replace(' ', '')):
                messages.error(request, 'Please use a valid phone number with a country code (e.g., +880...).')
                return redirect('home')

        # Email Validation (MX Record Check via email-validator)
        try:
            from email_validator import validate_email, EmailNotValidError
            # check_deliverability=True performs DNS MX checks
            valid_email_info = validate_email(email, check_deliverability=True)
            email = valid_email_info.normalized
        except EmailNotValidError:
            messages.error(request, 'Please use a valid and existing email address.')
            return redirect('home')

        # Google reCAPTCHA Validation
        recaptcha_response = request.POST.get('g-recaptcha-response')
        if not recaptcha_response:
            messages.error(request, 'Please complete the reCAPTCHA to verify you are human.')
            return redirect('home')

        data = {
            'secret': settings.RECAPTCHA_SECRET_KEY,
            'response': recaptcha_response
        }
        r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
        result = r.json()

        if not result.get('success'):
            messages.error(request, 'Invalid reCAPTCHA. Please try again.')
            return redirect('home')

        try:
            ContactMessage.objects.create(
                name=name,
                email=email,
                company=company,
                phone=phone,
                service=service_value,
                message=message
            )
            messages.success(
                request,
                'Thank you! Your message has been sent successfully. We will get back to you soon.')
        except Exception:
            messages.error(
                request,
                'An error occurred while sending your message. Please try again later.')

        return redirect('home')

    services = cache.get('home_services')
    if not services:
        services = list(Service.objects.all())
        cache.set('home_services', services, 3600)

    team_members = cache.get('home_team_members')
    if not team_members:
        team_members = list(TeamMember.objects.all())
        cache.set('home_team_members', team_members, 3600)

    context = {
        'services': services,
        'team_members': team_members,
        'recaptcha_site_key': settings.RECAPTCHA_SITE_KEY,
    }
    return render(request, 'core/home.html', context)
