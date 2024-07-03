from django.db import models

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length = 100)
    
class Restaurant(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_DEFAULT, default = 7)
    # category는 외래키로 사용. 삭제 시에는 기본값인 7번 (기본 그룹) 으로 자동으로 설정됨.
    # 이후 식당이름 / 링크 등의 정보는 카테고리만 기본 그룹으로 변경된 상태로 보존된다.
    # 기타 - cascade는 연쇄삭제. protect는 하위 요소가 있는 경우 에러가 발생해 삭제되지 않음.(ProtectedError) / SET_NULL인 경우 참조값이 NULL로 변경됨.
    restaurant_name = models.CharField(max_length = 100)
    restaurant_link = models.CharField(max_length = 500)
    restaurant_content = models.TextField()
    restaurant_keyword = models.CharField(max_length = 50)
        