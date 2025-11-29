from django.shortcuts import render, get_object_or_404
from .models import Product
from django.contrib import messages
from django.shortcuts import redirect, reverse
from django.db.models import Q
from .models import Product, categories


# Create your views here.

def all_products(request):
    products = Product.objects.all()
    query = None
    categories_param = None
    current_categories = None

    # ---- Search Queries ----
    if 'q' in request.GET:
        query = request.GET['q']
        if not query:
            messages.error(request, "You didn't enter any search criteria!")
            return redirect(reverse('products'))

        queries = Q(name__icontains=query) | Q(description__icontains=query)
        products = products.filter(queries)

    # ---- categories Filtering ----
    if 'categories' in request.GET:
        categories_param = request.GET['categories']  # e.g., "jeans,shirts"
        categories_list = categories_param.split(',')  # ['jeans', 'shirts']
        products = products.filter(categories__name__in=categories_list)

        # Get categories objects for template
        current_categories = categories.objects.filter(name__in=categories_list)

    context = {
        'products': products,
        'search_term': query,
        'current_categories': current_categories,
    }

    return render(request, 'products/products.html', context)




def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)