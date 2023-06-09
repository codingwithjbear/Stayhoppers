from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import listingInfo

# Create your views here.

def hello_world(request):
    return HttpResponse("Hello, world!")

def all_listings(request):
    listings = listingInfo.objects.all()
    data = []
    for listing in listings:
        listing_data = {
            'id': listing.id,
            'title': listing.title,
            'description': listing.description,
            'price': str(listing.price),
            'bedrooms': listing.bedrooms,
            'bathrooms': str(listing.bathrooms),
            'sqft': listing.sqft,
            'photo': listing.photo.url,
            'is_published': listing.is_published,
            'list_date': listing.list_date.strftime('%Y-%m-%d %H:%M:%S')
        }
        data.append(listing_data)

    return JsonResponse(data, safe=False)
 
