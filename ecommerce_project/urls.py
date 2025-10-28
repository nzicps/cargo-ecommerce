from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from ecommerce_project import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/home/')),
    path('home/', views.home, name='home'),
    path('accounts/', include('accounts.urls')),
    path('cart/', include('cart.urls')),
    path('catalog/', include('catalog.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('orders/', include('orders.urls')),
    path('payments/', include('payments.urls')),
    path('shipping/', include('shipping.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from cargo_app import views  # added automatically

urlpatterns += [
    path('api/test-middleware/', views.test_middleware),
]
