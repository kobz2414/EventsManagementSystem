from django.shortcuts import render, redirect
from .models import event
from .forms import addAndEditForm

def listings(request):
    if request.method == 'POST':
        form = addAndEditForm(request.POST or None) 
        if form.is_valid():
            form.save()
            events = event.objects.all()
            context = {'events': events}
            return render(request, 'list_page.html', context)
    else:
        events = event.objects.all()
        context = {'events': events}
        return render(request, 'list_page.html', context)

def delete(request, list_id):
    item = event.objects.get(pk=list_id) 
    item.delete() 
    return redirect('listings')

def edit(request, list_id):
    if request.method == 'POST':
        event_item = event.objects.get(pk=list_id) 
        form = addAndEditForm(request.POST or None)
        if form.is_valid ():
            event_name = form.cleaned_data.get("event_name")
            event_location = form.cleaned_data.get("event_location")
            event_date = form.cleaned_data.get("event_date")
            event_remarks = form.cleaned_data.get("event_remarks")
            pricing = form.cleaned_data.get("pricing")
            event_item.event_name = event_name 
            event_item.event_location = event_location
            event_item.event_date = event_date 
            event_item.event_remarks = event_remarks 
            event_item.pricing = pricing 
            event_item.save() 
            return redirect('listings')
    else:
        event_item = event.objects.get(pk=list_id) 
        context = {"list_id" : list_id, "event_item": event_item} 
        return render (request, 'edit.html', context)
