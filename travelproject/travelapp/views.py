from django.http import HttpResponse
from django.shortcuts import render
from .models import Place
from .models import Team


# Create your views here.
def demo(request):
    obj=Place.objects.all()

    obj2=Team.objects.all()

    return render(request, 'index.html',{'result':obj,'result2':obj2})


# def operation(request):
#     x = int(request.GET['num1'])
#     y = int(request.GET['num2'])
#     add1 = float(x + y)
#     sub1 = float(x - y)
#     mul1 = float(x * y)
#     div1 = float(x / y)
#
#
#     return render(request, "result.html", {'result1': add1,'result2':sub1,'result3':mul1,'result4':div1 })

