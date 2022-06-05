from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Food, Consume
def home(request):
    return render(request,'index.html')

def bmi(request):
    val1=int(request.POST['num1'])
    val2=float(request.POST['num2'])
    res=val1/(val2*val2)
    return render(request,'result.html',{'result':res})    


def index(request):

    if request.method == "POST":
        food_consumed = request.POST['food_consumed']
        consume = Food.objects.get(name=food_consumed)
        user = request.user
        consume = Consume(user=user, food_consumed=consume)
        consume.save()
        foods = Food.objects.all()

    else:
        foods = Food.objects.all()
    consumed_food = Consume.objects.filter(user=request.user)

    return render(request, 'caloriecalculator.html', {'foods': foods, 'consumed_food': consumed_food})


def delete_consume(request, id):
    consumed_food = Consume.objects.get(id=id)
    if request.method == 'POST':
        consumed_food.delete()
        return redirect('/user')
    return render(request, 'delete.html')

