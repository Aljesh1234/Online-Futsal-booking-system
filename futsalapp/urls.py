from django.contrib import admin
from django.urls import path,include
from .import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name='index'),
    path('booking',views.booking, name='booking'),
    path('detail',views.detail, name='detail'),
    path("update/<str:id>",views.update,name="update"),
    path("delete/<str:id>",views.delete,name='delete'),
]