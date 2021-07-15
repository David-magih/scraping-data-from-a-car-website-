from django.shortcuts import render
from json import JSONEncoder
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from web.models import User, Token, Car, Deal


@csrf_exempt
# Create your views here.
def submit_car(request):
    "submit a car "

    if request.method == "POST":
        this_year=request.POST['year']
        this_make=request.POST['make']
        this_model=request.POST['model']
        this_mileage=request.POST['mileage']
        #if year and make and model and mileage:
        if 1:

            Car.objects.create(year=this_year,make=this_make,model=this_model,mileage=this_mileage)

    print(request.POST)
    return JsonResponse({
        'status': 'OK'
    }, encoder=JSONEncoder

    )
