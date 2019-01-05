import csv
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import View
import urllib.request
import json
from parser4.models import Twogis

class View(View):
    def parse(request, *args, **kwargs):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'

        writer = csv.writer(response)
        writer.writerow(['oid', 'address', 'name', 'lat', 'lon'])
        twogiss = Twogis.objects.all()
        for twogis in twogiss:
            writer.writerow([twogis.oid, twogis.address, twogis.name, twogis.lat, twogis.lon])
        return response
    def truncate(request, *args, **kwargs):
        Twogis.objects.all().delete()
        return HttpResponse('sad')
    def count(request, *args, **kwargs):
        return HttpResponse(len(Twogis.objects.all()))