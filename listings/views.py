from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Listing
from listings.choices import bedroom_choices, state_choices, price_choices


# Create your views here.

# controllers for listings
def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    # pagination
    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    # pass in the context dictionary to the render
    # life can be so easy yet we complicate it.
    context = {
        'listings': paged_listings
    }
    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
    # get single listing from db get or 404

    listing = get_object_or_404(Listing, pk=listing_id)
    context = {
        'listing': listing
    }
    return render(request, 'listings/listing.html', context)


def search(request):
    # query_set list
    queryset_list = Listing.objects.order_by('-list_date')
    # keywords
    if 'keywords' in request.GET:
        keywords = request.GET.get('keywords')
        if keywords:
            # icontains checks if the selected property contains keyword
            queryset_list = queryset_list.filter(description__icontains=keywords)
    # city
    if 'city' in request.GET:
        city = request.GET.get('city')
        if city:
            #
            queryset_list = queryset_list.filter(city__iexact=city)
    # state

    if 'state' in request.GET:
        state = request.GET.get('state')
        if state:
            #
            queryset_list = queryset_list.filter(state__iexact=state)

    # bedroom
    if 'bedrooms' in request.GET:
        bedrooms = request.GET.get('bedrooms')
        if bedrooms:
            #
            queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)
    # price
    if 'price' in request.GET:
        price = request.GET.get('price')
        price = float(price.replace(',', ''))
        if price:
            #
            queryset_list = queryset_list.filter(price__lte=price)

    context = {
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'listings': queryset_list
    }
    return render(request, 'listings/search.html', context)
