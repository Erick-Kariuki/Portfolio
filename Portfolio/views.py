from Website import settings
from django.shortcuts import render
from django.http import JsonResponse
from django.core.mail import send_mail
from Portfolio.forms import ContactForm


def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            try:
                send_mail(
                    subject=form.cleaned_data['subject'],
                    message=f"""
Name: {form.cleaned_data['name']}
Email: {form.cleaned_data['email']}

Message:
{form.cleaned_data['message']}
                    """,
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[settings.EMAIL_HOST_USER],
                    fail_silently=False,
                )

                if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                    return JsonResponse({'success': True})

                form = ContactForm()

            except Exception as e:
                if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                    return JsonResponse(
                        {'success': False, 'error': 'Email failed to send.'},
                        status=500
                    )

    else:
        form = ContactForm()

    return render(request, 'index.html', {'form': form})


def mydairyfarm(request):
    return render(request, 'mydairyfarm.html')
def iothealthsystem(request):
    return render(request, 'iothealthsystem.html')
def weatherapp(request):
    return render(request, 'weatherapp.html')