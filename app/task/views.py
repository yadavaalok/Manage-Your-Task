from core.models import Event
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from datetime import datetime
from django.db.models import Q
from openpyxl import Workbook


def create_excel_sheet(events):
	wb = Workbook()
	ws = wb.active
	ws.append(["Event Title", "Event Type", "Event Status", "Event Date", "Description"])
	for event in events:
		event_date = event.event_date.replace(tzinfo=None)
		ws.append([event.event_title, event.event_type, event.event_status, event_date, event.event_description])
	
	return wb


class Index(View):

	def get(self, request):

		upcoming_events = Event.objects.filter(event_status="ACTIVE").order_by('event_date')[:2]
		present_month_events = Event.objects.filter(event_date__month=datetime.now().month) & Event.objects.filter(event_status="ACTIVE")
		cancelled_events = Event.objects.filter(event_status="CANCELLED").order_by('event_date')[:5]
		done_events = Event.objects.filter(event_status="DONE").order_by('-event_date')[:3]

		# list_by_status = {"status": [], "count": []}
		# for status in ["ACTIVE", "DONE", "CANCELLED", "UNKNOWN"]:
		# 	data = Event.objects.filter(event_status=status)
		# 	count = data.count()
		# 	list_by_status["status"].append(status)
		# 	list_by_status["count"].append(count)

		return render(request, 'dashboard.html', {'upcoming_events': upcoming_events, 'present_month_events': present_month_events, 'cancelled_events': cancelled_events, 'done_events': done_events})


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
	

class EventReports(View):

	def get(self, request, period):

		statuses = {"ACTIVE": [], "DONE": [], "CANCELLED": [], "UNKNOWN": []}

		corporate_event_q = Q(event_type__in=["Conferences", "Seminars", "Company Party/Meetings", "Product/Service Launch"])
		non_corporate_event_q = Q(event_type__in=["Weddings", "Festivals", "Exhibitions", "Charity Events", "Sports & Competitions"])
		
		if period == "MONTHLY":
			
			date_q = Q(event_date__month=datetime.now().month)
			
			for status in statuses.keys():

				status_q = Q(event_status=status)
				
				wb1 = create_excel_sheet(list(Event.objects.filter(status_q & date_q)))
				r1 = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
				r1['Content-Disposition'] = 'attachment; filename="allevents.xlsx"'
				wb1.save(r1)
				statuses[status].append(r1)
				wb2 = create_excel_sheet(list(Event.objects.filter(status_q & corporate_event_q & date_q)))
				r2 = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
				r2['Content-Disposition'] = 'attachment; filename="corporate.xlsx"'
				wb2.save(r2)
				statuses[status].append(r2)
				wb3 = create_excel_sheet(list(Event.objects.filter(status_q & non_corporate_event_q & date_q)))
				r3 = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
				r3['Content-Disposition'] = 'attachment; filename="noncorporate.xlsx"'
				wb3.save(r3)
				statuses[status].append(r3)

			return render(request, 'reports.html', {'statuses': statuses})
		elif period == "QUARTERLY":
			return render(request, 'reports.html')
		elif period == "HALF YEARLY":
			return render(request, 'reports.html')
		else:
			return render(request, 'reports.html')
