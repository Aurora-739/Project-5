from django.shortcuts import render, get_object_or_404
from .models import Product, Category 
from django.contrib import messages
from django.shortcuts import redirect
from django.db.models import Q
from django.db.models.functions import Lower

def all_products(request):
    products = Product.objects.all()
    query = None
    current_categories = None
    sort = None
    direction = None

    # --- Handle search query ---
    if 'q' in request.GET:
        query = request.GET['q']
        if query:
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)
        else:
            messages.error(request, "You didn't enter any search criteria!")
            return redirect('products')

    # --- Handle category filtering ---
    if 'categories' in request.GET:
        current_categories = request.GET['categories'].split(',')
        products = products.filter(categories__name__in=current_categories).distinct()

    # --- Handle sorting ---
    if 'sort' in request.GET:
        sort = request.GET['sort']
        direction = request.GET.get('direction', 'ascending')
        sortkey = sort

        # Special case for name: case-insensitive
        if sort == 'name':
            products = products.annotate(lower_name=Lower('name'))
            sortkey = 'lower_name'

        # Special case for category
        if sortkey == 'category':
            sortkey = 'categories__name'


        # Reverse order if descending
        if direction == 'descending':
            sortkey = f'-{sortkey}'

        products = products.order_by(sortkey)

    # --- Pass current sorting to template ---
    current_sorting = f'{sort}_{direction}' if sort and direction else 'none_none'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': current_categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)

def product_detail(request, product_id):
    """ Show individual product details """
    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)
