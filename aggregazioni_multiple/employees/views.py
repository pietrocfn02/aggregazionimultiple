from django.shortcuts import render
from .utils import update_filters, update_tables
# Create your views here.




def homepage(request, filters=''):
    #print("###############"+str(filters))
    
    update = True
    nextNoFilter = False


    if request.GET.get('nextNoFilter', default=False):
        nextNoFilter = True
    
    if request.GET.get('noupdate', default=False):
        update = False

    header = []
    filter_array = []
    remaining = []
    if request.GET.get('add', default=None) != None:
        filters+=','+request.GET.get('add')
        

    table = []
    
    if not update:
        res = update_tables(table=table,filter_array=filter_array)
        header = res[0]
        table = res[1]
    
    res = update_filters(filters,filter_array,remaining)
    filter_array = res[0]
    remaining = res[1]
    
    
    if update:
        res = update_tables(table=table,filter_array=filter_array)
        header = res[0]
        table = res[1]

    context = {"header": header, "timereports" : table, "filters" : filter_array, "available_filters" : remaining, "filterstring" : filters, "nextNoFilter" : nextNoFilter}
    
    return render(request, "home.html", context)