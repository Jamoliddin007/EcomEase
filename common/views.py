from django.views.generic import TemplateView # htmlni render qilib beradi template larni view qilib beradi
from products.models import Category,Product
class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = Category.objects.all()


        context['title'] = 'VooComerce'
        context['categories'] = categories
        return context
    
class ContactView(TemplateView):
    template_name = 'contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Contact Us'
        return context
    

class BlogView(TemplateView):
    template_name = 'blog.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Blog'
        return context
    
class BlogDetailView(TemplateView):
    template_name = 'blog-details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Blog Detail'
        return context
    
class CheckoutView(TemplateView):
    template_name = 'checkout.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Checkout'
        return context
    
class MainView(TemplateView):
    template_name = 'main.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Main'
        return context
    
class ShopDetailView(TemplateView):
    template_name = 'shop-details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Shop Detail'
        return context
    
class ShopGridView(TemplateView):
    template_name = 'shop-grid.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Shop Grid'
        return context
    
class ShopingCartView(TemplateView):
    template_name = 'shoping-cart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Shopping Cart'
        return context
