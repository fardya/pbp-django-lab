from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from mywatchlist.models import WatchList

def show_watchlist(request):
    return render(request, "mywatchlist.html", context)

data_tontonan = WatchList.objects.all()
context = {
    'list_tontonan': data_tontonan,
    'nama': 'Davina',
    'student ID': '2106702005'
}

def show_xml(request):
    data = WatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = WatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_html(request):
    return render(request, 'watchedlist.html', contextHtml)

contextHtml = {
    'list_tontonan': data_tontonan 
}

def show_json_by_id(request, id):
    data = WatchList.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = WatchList.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")