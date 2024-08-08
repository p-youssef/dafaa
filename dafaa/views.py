from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from production.models import *
from records.models import *
import datetime
from django.db.models import Sum


def home(request):
    return render(request, 'home.html')


@user_passes_test(lambda user: user.is_superuser)
def management_dashboard(request):

    this_year = datetime.date.today().year

    this_year_selles = Selling_Record.objects.filter(selling_date__year=this_year)

    
    revenue = sum([ s.price for s in this_year_selles ]) 
    profit = sum([ s.item.get_profit_value() for s in this_year_selles ])


    data = {
        'products': Product.objects.all(),
        'available_items':Product_Item.objects.filter(selled = False, preduced = True),
        'sold_items':Product_Item.objects.filter(selled = True),
        'preduced_items':Product_Item.objects.filter(preduced = True),
        'producing':  Product_Item.objects.filter(preduced = False),
        'packages': Package_S2I.objects.all(),
        'unsend_packages': Package_S2I.objects.filter(send = False),
        'send_packages': Package_S2I.objects.filter(send = True),
        'this_year': this_year,
        'revenue': revenue,
        'profit':profit,
        'spending': revenue - profit,
    }

    return render(request, 'management_dashboard.html', data)

