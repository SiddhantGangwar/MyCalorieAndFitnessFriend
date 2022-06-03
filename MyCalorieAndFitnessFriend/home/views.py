from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    return render(request,'index.html')

def bmi(request):
    val1=int(request.POST['num1'])
    val2=float(request.POST['num2'])
    res=val1/(val2*val2)
    return render(request,'result.html',{'result':res})    