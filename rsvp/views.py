from django.shortcuts import render, redirect
from .models import Guest
from datetime import datetime

def startseite(request):
    return render(request, 'start.html')

def index(request):
    if request.method == 'POST':
        name = request.POST['name']
        attendance = request.POST['attendance']

        if attendance == 'Ich nehme teil':
            guests_count = int(request.POST['guests'])
        else:
            guests_count = 0

        rsvp_date = datetime.utcnow()

        new_guest = Guest(name=name, guests=guests_count, attendance=attendance, rsvp_date=rsvp_date)
        new_guest.save()

        return redirect('confirmation')

    return render(request, 'index.html')

def confirmation(request):
    return render(request, 'confirmation.html')

def guest_summary(request):
    attending_count = Guest.objects.filter(attendance='Ich nehme teil').count()
    not_attending_count = Guest.objects.filter(attendance='Ich nehme nicht teil').count()

    context = {
        'attending_count': attending_count,
        'not_attending_count': not_attending_count,
    }

    return render(request, 'admin/guest_summary.html', context)
