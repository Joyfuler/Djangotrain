# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import *


def index(request):    
    categories = Category.objects.all()
    restaurants = Restaurant.objects.all()
    content = {
        'categories' : categories,
        'restaurants' : restaurants
    }   
    
    return render(request, 'shareRes/index.html', content)

def restaurantDetail(request, res_id):    
    restaurant = Restaurant.objects.get(id = res_id)
    content = {
        'restaurant': restaurant        
    }       
    return render(request, 'shareRes/restaurantDetail.html', content) # content 딕셔너리 형태를 render 함수에 담아 전달.

def restaurantUpdate(request, res_id):    
    categories = Category.objects.all()
    restaurant = Restaurant.objects.get(id = res_id)
    content = {
        'categories' : categories,
        'restaurant' : restaurant
    }    
    return render(request, 'shareRes/restaurantUpdate.html', content)  

def Update_restaurant(request):
    resId = request.POST['resId']
    change_category_id = request.POST['resCategory']
    change_category = Category.objects.get(id = change_category_id)
    change_name = request.POST['resTitle']
    change_link = request.POST['resLink']
    change_content = request.POST['resContent']
    change_keyword = request.POST['resLoc']
    before_restaurant = Restaurant.objects.get(id = resId)
    before_restaurant.category = change_category
    before_restaurant.restaurant_name = change_name
    before_restaurant.restaurant_link = change_link
    before_restaurant.restaurant_content = change_content
    before_restaurant.restaurant_keyword = change_keyword
    before_restaurant.save()
    return HttpResponseRedirect(reverse('resDetailPage', 
                                        kwargs= {
                                            'res_id' : resId
                                            }
                                        ))


def Delete_restaurant(request):
    res_id = request.POST['resId']
    restaurant = Restaurant.objects.get(id = res_id)
    restaurant.delete()
    return HttpResponseRedirect(reverse('index'))

def restaurantCreate(request):
    categories = Category.objects.all()
    restaurants = Restaurant.objects.all()
    content = {
        'categories' : categories,
        'restaurants' : restaurants
    }
    return render(request, 'shareRes/restaurantCreate.html', content)

def Create_restaurant(request):
    category_id = request.POST['resCategory']
    category = Category.objects.get(id = category_id) # 해당 카테고리 id를 가진 객체를 모두 가져온다.
    name = request.POST['resTitle']
    link = request.POST['resLink']
    content = request.POST['resContent']
    keyword = request.POST['resLoc']
    new_res = Restaurant(category = category, restaurant_name = name, 
                         restaurant_link = link, restaurant_content = content,
                         restaurant_keyword = keyword)
    
    new_res.save()
    return HttpResponseRedirect(reverse('index')) # 처리를 완료한 후 메인 페이지로 돌아감.  

def categoryCreate(request):
    categories = Category.objects.all()
    content = { 
        'categories' : categories           
    }
    return render(request, 'shareRes/categoryCreate.html', content)

def Create_category(request):
    category_name = request.POST['categoryName']
    new_category = Category(category_name = category_name)
    new_category.save()
    return HttpResponseRedirect(reverse('index')) #다시 돌아가는 함수

def Delete_category(request):
    category_id = request.POST['categoryId']
    delete_category = Category.objects.get(id = category_id)
    delete_category.delete()
    return HttpResponseRedirect(reverse('cateCreatePage'))