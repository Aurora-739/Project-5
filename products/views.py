# products/views.py
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q, Avg
from django.db.models.functions import Lower, Coalesce
from .models import Product, Category, Review, Wishlist
from .forms import ReviewForm, ProductForm


def all_products(request):
    """Show all products with sorting and searching"""
    products = Product.objects.annotate(avg_rating=Coalesce(Avg('reviews__rating'), 0.0))
    query = None
    current_categories = None
    sort = None
    direction = None

    if 'q' in request.GET:
        query = request.GET['q']
        if query:
            queries = Q(name__icontains=query) | Q(description__icontains=query) | Q(categories__name__icontains=query) | Q(categories__friendly_name__icontains=query)
            products = products.filter(queries).distinct()
        else:
            messages.error(request, "You didn't enter any search criteria!")
            return redirect('products:all_products')

    if 'categories' in request.GET:
        current_categories = request.GET['categories'].split(',')
        products = products.filter(categories__name__in=current_categories).distinct()

    if 'sort' in request.GET:
        sort = request.GET['sort']
        direction = request.GET.get('direction', 'ascending')
        sortkey = sort

        if sort == 'name':
            products = products.annotate(lower_name=Lower('name'))
            sortkey = 'lower_name'

        if sort == 'rating':
            sortkey = 'avg_rating'

        if sortkey == 'category':
            sortkey = 'categories__name'

        if direction == 'descending':
            sortkey = f'-{sortkey}'

        products = products.order_by(sortkey)

    current_sorting = f'{sort}_{direction}' if sort and direction else 'none_none'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': current_categories,
        'current_sorting': current_sorting,
        'all_categories': Category.objects.all(),
    }

    return render(request, 'products/products.html', context)


def product_detail(request, sku):
    """Show individual product details and reviews"""
    product = get_object_or_404(Product, sku=sku)
    reviews = product.reviews.all().order_by('-created_at')
    user_review = None
    review_form = ReviewForm()
    edit_review_form = None

    if request.user.is_authenticated:
        user_review = Review.objects.filter(
            product=product, user=request.user
        ).first()
        edit_review_form = ReviewForm(instance=user_review) if user_review else None

    context = {
        'product': product,
        'reviews': reviews,
        'review_form': review_form,
        'edit_review_form': edit_review_form,
        'user_review': user_review,
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def add_review(request, sku):
    """Add a review for a product"""
    product = get_object_or_404(Product, sku=sku)

    if Review.objects.filter(product=product, user=request.user).exists():
        messages.error(request, 'You have already reviewed this product.')
        return redirect(reverse('products:product_detail', args=[sku]))

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.user = request.user
            review.save()
            messages.success(request, 'Your review has been added!')
        else:
            messages.error(request, 'There was an error with your review.')

    return redirect(reverse('products:product_detail', args=[sku]))


@login_required
def edit_review(request, sku, review_id):
    """Edit an existing review"""
    product = get_object_or_404(Product, sku=sku)
    review = get_object_or_404(Review, id=review_id, user=request.user)

    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your review has been updated!')
        else:
            messages.error(request, 'There was an error updating your review.')

    return redirect(reverse('products:product_detail', args=[sku]))


@login_required
def delete_review(request, sku, review_id):
    """Delete a review"""
    review = get_object_or_404(Review, id=review_id, user=request.user)
    review.delete()
    messages.success(request, 'Your review has been deleted!')
    return redirect(reverse('products:product_detail', args=[sku]))


@login_required
def wishlist(request):
    """Display the user's wishlist"""
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)
    context = {
        'wishlist': wishlist,
    }
    return render(request, 'products/wishlist.html', context)


@login_required
def add_to_wishlist(request, sku):
    """Add a product to the user's wishlist"""
    product = get_object_or_404(Product, sku=sku)
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)
    if product in wishlist.products.all():
        messages.info(request, f'{product.name} is already in your wishlist!')
    else:
        wishlist.products.add(product)
        messages.success(request, f'{product.name} added to your wishlist!')

    return redirect(reverse('products:product_detail', args=[sku]))


@login_required
def remove_from_wishlist(request, sku):
    """Remove a product from the user's wishlist"""
    product = get_object_or_404(Product, sku=sku)
    wishlist = get_object_or_404(Wishlist, user=request.user)
    wishlist.products.remove(product)
    messages.success(request, f'{product.name} removed from your wishlist!')
    return redirect(reverse('products:wishlist'))


@login_required
def add_product(request):
    """Superuser-only view to add a new product"""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('products:all_products'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Product added successfully!')
            return redirect(reverse('products:product_detail', args=[product.sku]))
        else:
            messages.error(request, 'Failed to add product. Please check the form.')
    else:
        form = ProductForm()

    return render(request, 'products/add_product.html', {'form': form})


@login_required
def edit_product(request, sku):
    """Superuser-only view to edit an existing product"""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('products:all_products'))

    product = get_object_or_404(Product, sku=sku)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product updated successfully!')
            return redirect(reverse('products:product_detail', args=[product.sku]))
        else:
            messages.error(request, 'Failed to update product. Please check the form.')
    else:
        form = ProductForm(instance=product)

    return render(request, 'products/edit_product.html', {'form': form, 'product': product})


@login_required
def delete_product(request, sku):
    """Superuser-only view to delete a product"""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('products:all_products'))

    product = get_object_or_404(Product, sku=sku)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products:all_products'))
