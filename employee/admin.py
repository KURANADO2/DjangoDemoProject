from django.contrib import admin
from employee.models import Employee
from employee.models import Product

# Register your models here.


# 员工管理类
class EmployeeAdmin(admin.ModelAdmin):
    # 显示那些字段
    list_display = ['id', 'code', 'name']
    # 可以根据哪些字段进行搜索
    search_fields = ['code', 'name']
    # 哪些字段可以被过滤
    list_filter = ['id']


# 商品管理类
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'amount', 'is_publish', 'create_time', 'update_time']
    search_fields = ['name', 'price', 'amount', 'is_publish', 'create_time', 'update_time']
    list_filter = ['id', 'name', 'price', 'amount', 'is_publish', 'create_time', 'update_time']


# 注册雇员对象模型到 admin 中
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Product, ProductAdmin)
