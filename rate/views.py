from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import Rate, Currency
from bitrate.basic_auth import basic_auth

@basic_auth
def currencies(request):
    # выведет список валют 
    limit = request.GET.get('limit', 10)
    page = request.GET.get('page', 0)
    if limit and str(limit).isdigit():
        limit = int(limit)
    if page and str(page).isdigit():
        page = int(page)
    return JsonResponse({"result": Currency.get_list(limit, page)})

@basic_auth
def rate(request, currency_id):
    return JsonResponse({"result": {"rate": Rate.get_last_rate(currency_id)}, "mean_volume": Rate.get_mean_volume(currency_id)})

def refresh(request):
    if request.user.is_authenticated:
        Rate.refresh_all()
    return HttpResponse(status=200)