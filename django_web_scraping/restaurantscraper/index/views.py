from django.shortcuts import render
from models import Restaurant
from tasks import yelp_restaurants
# Create your views here.
def view(request):
    restaurants = yelp_restaurants()
    html =  "<html><body>%s</body></html>" % restaurants
    return HttpResponse(html)
