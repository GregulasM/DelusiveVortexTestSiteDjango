from django.contrib import admin
from django.urls import path, include, reverse_lazy
from catalog import views
from catalog.views import UserLoginView, UserProfileView
from django.contrib.auth.views import LogoutView
from catalog.views import add_to_cart

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('maps/', views.maps, name='maps'),
    path('world_maps/', views.world_maps, name='world_maps'),
    path('about/', views.about, name='about'),
    path('search/', views.search, name='search'),
    path('accounts/profile/', UserProfileView.as_view(), name='profile'),
    path('register/', views.register, name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page=reverse_lazy('home')), name='logout'),
]
