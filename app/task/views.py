from core.models import Event
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from datetime import datetime

class Index(View):

	def get(self, request):

		upcoming_events = Event.objects.filter(event_status="ACTIVE").order_by('event_date')[:2]
		present_month_events = Event.objects.filter(event_date__month=datetime.now().month) & Event.objects.filter(event_status="ACTIVE")
		cancelled_events = Event.objects.filter(event_status="CANCELLED").order_by('event_date')[:5]
		done_events = Event.objects.filter(event_status="DONE").order_by('-event_date')[:3]

		list_by_status = {"status": [], "count": []}
		for status in ["ACTIVE", "DONE", "CANCELLED", "UNKNOWN"]:
			data = Event.objects.filter(event_status=status)
			count = data.count()
			list_by_status["status"].append(status)
			list_by_status["count"].append(count)

		print(list_by_status)
		return render(request, 'dashboard.html', {'upcoming_events': upcoming_events, 'present_month_events': present_month_events, 'cancelled_events': cancelled_events, 'done_events': done_events, 'list_by_status': list_by_status})


class CreateEvent(View):

	def get(self, request):
		return render(request, 'event.html')

	def post(self, request):
		data = request.POST
		event_title = data.get('title')
		event_type = data.get('eventtype')
		event_status = data.get('eventstatus')
		event_date = data.get('datetime')
		event_description = data.get('description')

		event = Event(event_title=event_title, event_type=event_type, event_status=event_status, event_date=event_date, event_description=event_description)

		event.save()
		return redirect('homepage')


class ListEventByType(View):

	def get(self, request, event_type):
		if event_type == 'corporate':
			events = Event.objects.filter(event_type__in=["Conferences", "Seminars", "Company Party/Meetings", "Product/Service Launch"])
		elif event_type == 'noncorporate':
			events = Event.objects.filter(event_type__in=["Weddings", "Festivals", "Exhibitions", "Charity Events", "Sports & Competitions"])
		else:
			events = Event.objects.all()

		return render(request, 'allevents.html', {'events': events})


class ListEventByStatus(View):

	def get(self, request, event_status):
		if event_status == 'ACTIVE':
			events = Event.objects.filter(event_status="ACTIVE")
		elif event_status == 'DONE':
			events = Event.objects.filter(event_status='DONE')
		elif event_status == 'CANCELLED':
			events = Event.objects.filter(event_status='CANCELLED')
		else:
			events = Event.objects.filter(event_status='UNKNOWN')

		return render(request, 'allevents.html', {'events': events})


class DeleteEvent(View):

    def post(self, request, pk):
        event = Event.objects.get(pk=pk)
        event.delete()
        return redirect('allevents', event_type='all')


class UpdateEvent(View):

	def get(self, request, pk):
		event = Event.objects.get(pk=pk)
		return render(request, 'editevent.html', {'event': event})

	def post(self, request, pk):
		event = Event.objects.get(pk=pk)

		event.event_title = request.POST.get('title')
		event.event_type = request.POST.get('eventtype')
		event.event_status =request.POST.get('eventstatus')
		event.event_date = request.POST.get('datetime')
		event.event_description = request.POST.get('description')

		event.save()

		return redirect('allevents', event_type='all')
