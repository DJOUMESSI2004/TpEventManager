from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Event, Participation
from .forms import ParticipationForm

def event_list(request):
    events = Event.objects.order_by('date')
    return render(request, 'events/event_list.html', {'events': events})

def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    form = None
    participation = None

    if request.user.is_authenticated:
        participation, _ = Participation.objects.get_or_create(user=request.user, event=event)
        if request.method == 'POST':
            form = ParticipationForm(request.POST, instance=participation)
            if form.is_valid():
                form.save()
                return redirect('event_detail', event_id=event.id)
        else:
            form = ParticipationForm(instance=participation)

    return render(request, 'events/event_detail.html', {
        'event': event,
        'form': form,
        'can_participate': request.user.is_authenticated,
        'participation': participation,
    })
