from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, UserProfile, Order
from django.core.mail import send_mail
from django.conf import settings
import os
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib.auth import login

def home(request):
    return render(request, 'catalog/home.html')

def maps(request):
    return render(request, 'catalog/maps.html')

def world_maps(request):
    products = Product.objects.all()

    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        name = request.POST.get('name')
        email = request.POST.get('email')

        if product_id and name and email:
            product = Product.objects.get(id=product_id)

            message = f'Заказ товара:\n\nТовар: {product.name}\nИмя: {name}\nEmail: {email}'
            send_mail('Заказ мерча', message, settings.DEFAULT_FROM_EMAIL, [settings.DEFAULT_FROM_EMAIL])

            if request.user.is_authenticated:
                user_profile = UserProfile.objects.get(user=request.user)
                user_profile.cart.add(product)
                user_profile.save()

            return redirect('success')

    context = {'products': products}
    return render(request, 'catalog/world_maps.html', context)


def about(request):
    return render(request, 'catalog/about.html')

def add_to_cart(request):
   if request.method == 'POST':
       if request.user.is_authenticated:
           user = request.user
           profile = UserProfile.objects.get_or_create(user=user)
           product_id = request.POST.get('product_id')
           product = get_object_or_404(Product, id=product_id)
           profile.cart.add(product)


def search(request):
    query = request.GET.get('query', '')

    static_dir = os.path.join(settings.BASE_DIR, 'static', 'pages')

    results = []

    for file_name in os.listdir(static_dir):
        file_path = os.path.join(static_dir, file_name)
        
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            
            sentences = content.split('. ')

            for sentence in sentences:
                if query.lower() in sentence.lower():
                    results.append(sentence)

    context = {
        'query': query,
        'results': results,
    }

    return render(request, 'catalog/search_results.html', context)

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(user=user)
            login(request, user)
            return redirect('profile')
    else:
        form = UserCreationForm()
    return render(request, 'catalog/registration.html', {'form': form})


class UserLoginView(LoginView):
    template_name = 'catalog/login.html'
    redirect_authenticated_user = True


class UserProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'catalog/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        profile = UserProfile.objects.get(user=user)

        context['cart'] = profile.cart.all()
        return context
