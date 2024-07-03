from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('restaurantDetail/delete', views.Delete_restaurant, name = 'resDelete'),
    path('restaurantDetail/<str:res_id>', views.restaurantDetail, name = 'resDetailPage'),
    path('restaurantDetail/updatePage/update', views.Update_restaurant, name = 'resupdate'), # str:res_id와 중복되어 해석가능하므로 위에 적을것.
    path('restaurantDetail/updatePage/<str:res_id>', views.restaurantUpdate, name = 'resUpdatePage'),        
    path('restaurantCreate/', views.restaurantCreate, name = 'resCreatepage'),
    path('restaurantCreate/create', views.Create_restaurant, name = 'resCreatePage'),    
    path('categoryCreate/', views.categoryCreate, name = 'cateCreatePage'),
    path('categoryCreate/create', views.Create_category, name = 'cateCreate'),
    path('categoryCreate/delete', views.Delete_category, name = 'cateDelete'),    
    # path의 name은 reverse함수에서 매개변수로 사용하여 완료 후 돌아갈 경로로 사용 가능.
    
]