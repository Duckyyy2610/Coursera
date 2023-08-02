from django.contrib import admin
from django.urls import path, include
from. import views
from rest_framework import routers
from rest_framework.authtoken.views import ObtainAuthToken
router = routers.DefaultRouter()
router.register(r'tables', views.BookingViewSet)


from . import views
urlpatterns = [
    path('restaurant/booking/', include(router.urls)),
    path('menu/', views.MenuItemsView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
    path('api-get-token/', ObtainAuthToken.as_view())
]
