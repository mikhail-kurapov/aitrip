from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Trip, Waypoint

# Create your views here.

class TripList(ListView):
    model = Trip
    context_object_name = 'trip_list'

    def get_queryset(self):
        return Trip.objects.filter(good_point_cnt__range=(5, 10))


class TripDetail(DetailView):

    model = Trip
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(TripDetail, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['waypoint_list'] = Waypoint.objects.all()
        return context

class TripWaypointList(ListView):

    template_name = 'showtrip/trip_waypoints.html'

    def get_queryset(self):
        self.trip_id = get_object_or_404(Trip, pk=self.args[0])
        return Waypoint.objects.filter(trip_id=self.trip_id)
    
#def trip_list(request):
#    trips_all = Trip.objects.filter().order_by('src_id')
#    paginator = Paginator(trips_all, 25)
#    page = request.GET.get('page')
#    try:
#        trips = paginator.page(page)
#    except PageNotAnInteger:
#        # If page is not an integer, deliver first page.
#        trips = paginator.page(1)
#    except EmptyPage:
#        # If page is out of range (e.g. 9999), deliver last page of results.
#        trips = paginator.page(paginator.num_pages)
#    return render(request, 'showtrip/trip_list.html',  {'trips': trips})

#def trip_detail(request, pk):
#        trip = get_object_or_404(Trip, pk=pk)
#        waypoints = Waypoint.objects.filter(trip_id=pk)
#        , 'waypoints':waypoints}
#        return render(request, 'showtrip/trip_detail.html', {'trip': trip})
