from datetime import date
from django.shortcuts import render
import datetime

# Create your views here.
def home(request):
    date=datetime.datetime.now()
    msg='hello django'
    h=int(date.strftime('%H'))
    if h<12:
        msg=msg+"gm"
    elif h<16:
        msg=msg+"gnoon"
    elif h<21:
        msg=msg+"ge"
    else:
        msg=msg+"gn"
    d={'insertdata':msg,'insertdate':date}
    return render(request,'home1.html',context=d)
