from core.models import Event
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View

class Index(View):

	def get(self, request):
		return render(request, 'dashboard.html')
	

class CreateEvent(View):
	
	def get(self, request):
		return render(request, 'event.html')
	
	def post(self, request):
		data = request.POST
		event_title = data.get('title')
		event_type = data.get('eventtype')
		event_date = data.get('datetime')
		event_description = data.get('description')

		event = Event(event_title=event_title, event_type=event_type, event_date=event_date, event_description=event_description)

		event.save()
		return redirect('homepage')


class ListEvent(View):

	def get(self, request):
		events = Event.objects.all()
		return render(request, 'allevents.html', {'events': events})
	

class DeleteEvent(View):

    def post(self, request, pk):
        # Handle the deletion when the user confirms
        event = Event.objects.get(pk=pk)
        event.delete()
        return redirect('allevents')
    

class UpdateEvent(View):

	def get(self, request, pk):
		event = Event.objects.get(pk=pk)
		return render(request, 'editevent.html', {'event': event})
	
	def post(self, request, pk):
		event = Event.objects.get(pk=pk)

		event.event_title = request.POST.get('title')
		event.event_type = request.POST.get('eventtype')
		event.event_date = request.POST.get('datetime')
		event.event_description = request.POST.get('description')

		event.save()

		return redirect('allevents')


