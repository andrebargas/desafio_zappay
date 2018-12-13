from django.db import models

class Launch(models.Model):
    flight_number = models.IntegerField(blank=False, verbose_name="Flight ID")
    mission_name = models.CharField(max_length=80, blank=False, verbose_name="Mission Name")
    mission_patch = models.CharField(max_length=200, blank=False, verbose_name="Mission Patch")
    video_link = models.CharField(max_length=200, blank=False, verbose_name="Video Link")
    rocket_name = models.CharField(max_length=200, blank=False, verbose_name="Rocket Name")
    launch_date_utc = models.CharField(max_length=30, blank=False, verbose_name="Date UCT")
