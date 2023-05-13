from django.http import HttpResponse
from django.shortcuts import render
from .models import Place

# Create your views here.
def demo(request):
    obj = Place.objects.all()
    return render(request,'index.html',{'result':obj})
# def Mathematical_Operations(request):
#     x = int(request.GET['num1'])
#     y = int(request.GET['num2'])
#     ares = x+y
#     sres = x-y
#     mress = x*y
#     dress = x / y
#     return render(request, 'result.html', {'result1': ares, 'result2': sres, 'result3': mress, 'result4':dress})

