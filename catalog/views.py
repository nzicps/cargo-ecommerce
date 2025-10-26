from django.shortcuts import render

def catalog_home(request):
    # Temporary demo products — replace later with database models
    products = [
        {'name': 'Eco Tote Bag', 'description': 'Reusable bag made from recycled cotton.', 'price': 12.99, 'image_url': 'https://via.placeholder.com/150'},
        {'name': 'Solar Lantern', 'description': 'Portable light powered by clean solar energy.', 'price': 24.50, 'image_url': 'https://via.placeholder.com/150'},
        {'name': 'Bamboo Water Bottle', 'description': 'Sustainable and stylish bamboo bottle.', 'price': 18.00, 'image_url': 'https://via.placeholder.com/150'},
    ]
    return render(request, 'catalog/index.html', {'products': products})
