from django.db import models
#from django.contrib.postgres.fields import JSONField

# Create your models here.

class Country(models.Model):
    title = models.CharField(max_length=2000)
    
class Trip(models.Model):
    src_id = models.CharField(max_length=32)
    title = models.CharField(max_length=2000)
    started = models.DateField(default=None, blank=True, null=True)
    finished = models.DateField(default=None, blank=True, null=True)
    lat = models.FloatField(default=None, blank=True, null=True)
    lng = models.FloatField(default=None, blank=True, null=True)
    views = models.IntegerField(default=0)
    follow_cnt = models.IntegerField(default=0)
    thumbnail = models.TextField(default=None, blank=True, null=True)
    thumbnail_new = models.TextField(default=None, blank=True, null=True)
    good_point_cnt = models.IntegerField(default=0)
    score = models.IntegerField(default=0)
    duration_days = models.IntegerField(default=0)
    distance = models.FloatField(default=None, blank=True, null=True)
    isfullinfo = models.CharField(max_length=1,default=None, blank=True, null=True)
    pointsbitmap = models.CharField(max_length=64,default=None, blank=True, null=True)
    
#    jb = JSONField(default=None, blank=True, null=True)
#    published_date = models.DateTimeField(default=None, blank=True, null=True)
#    waypionts = [ Waypoint, ]

    def __str__(self):
        return self.title

class WaypointType(models.Model):
    title = models.CharField(max_length=1000)

#
class Point(models.Model):
    title = models.CharField(max_length=1000,default=None, blank=True, null=True)
    lat = models.FloatField(default=None, blank=True, null=True)
    lng = models.FloatField(default=None, blank=True, null=True)
    cnt = models.IntegerField(default=0)
    orderby = models.IntegerField(default=0)
    waypoint_type = models.ForeignKey(Country,default=None, blank=True, null=True, related_name='%(class)s_waypoint_type')
    country = models.ForeignKey(Country,default=None, blank=True, null=True, related_name='%(class)s_country')

# one point - many names
class PointName(models.Model):
    title = models.CharField(max_length=1000)
    lat = models.FloatField(default=None, blank=True, null=True)
    lng = models.FloatField(default=None, blank=True, null=True)
    cnt = models.IntegerField(default=0)
    point=models.ForeignKey(Point,default=None, blank=True, null=True, related_name='%(class)s_point')
    
class Waypoint(models.Model):
    trip = models.ForeignKey(Trip)
    title = models.CharField(max_length=1000)
    description = models.TextField(default=None, blank=True, null=True)
    notes = models.TextField(default=None, blank=True, null=True)
    address = models.CharField(max_length=1000, default=None, blank=True, null=True)
    more_info_url = models.TextField(default=None, blank=True, null=True)
    w_datetime = models.DateTimeField(default=None, blank=True, null=True)
#    w_date = models.DateField()
#    w_time = models.TimeField
    lat = models.FloatField(default=None, blank=True, null=True)
    lng = models.FloatField(default=None, blank=True, null=True)
    passthru = models.CharField(max_length=1) #models.BooleanField(default=None, blank=True)
    travel_mode = models.CharField(max_length=1000, default=None, blank=True, null=True)
    travel_path = models.TextField(default=None, blank=True, null=True)
    travel_dest = models.CharField(max_length=1000,default=None, blank=True, null=True)
    country = models.ForeignKey(Country,default=None, blank=True, null=True, related_name='%(class)s_country')
    waypoint_type = models.ForeignKey(Country,default=None, blank=True, null=True, related_name='%(class)s_waypoiny_type')
    point = models.ForeignKey(Point,default=None, blank=True, null=True, related_name='%(class)s_point')
    
class TripPoint(models.Model):
    trip = models.ForeignKey(Trip)
    title = models.CharField(max_length=1000, default=None, blank=True, null=True)
    lat = models.FloatField(default=None, blank=True, null=True)
    lng = models.FloatField(default=None, blank=True, null=True)
    duration = models.DurationField(default=None, blank=True, null=True)
    distance = models.FloatField(default=None, blank=True, null=True)
    point = models.ForeignKey(Point,default=None, blank=True, null=True, related_name='%(class)s_point')

    def __str__(self):
        return self.title



