from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Food, Consume, FoodManage
import requests
from django.contrib import messages
from django.contrib.auth.models import User, auth
def home(request):
    api_url = 'https://api.calorieninjas.com/v1/nutrition?query='
    query = '3lb carrots and a chicken sandwich'
    searchquery=request.GET.get('searchquery')
    print (searchquery)
    if searchquery is not None:
      query = searchquery
    response = requests.get(api_url + query, headers={'X-Api-Key': 'oUqvROZU7DmOYcEgLLLxFA==Oyih5zrrT6A2vFp7'})
    data=response.json()
    # print(data)
    # if response.status_code == requests.codes.ok:
    #    print(response.text)
    # else:
    #     print("Error:", response.status_code, response.text)
    items=data['items']
    context={
        'items':items
    }
    return render(request,'index.html',context)

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

def foodmanage(request):

    if request.method=='POST':
        name=request.POST['name']
        date=request.POST['date']
        eat=request.POST['eat']
        rating=request.POST['rating']
        fm = FoodManage.objects.create(name=name,date=date,rating=rating,eat=eat)
        return redirect('/')
        
    else:   
        return render(request,'foodmanage.html')