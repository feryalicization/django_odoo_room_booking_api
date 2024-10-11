from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from django.urls import path
from .views.users import CustomTokenObtainPairView, UserRegistrationView, UserEditView
from .views.ruangan import *



schema_view = get_schema_view(
    openapi.Info(
        title="Odoo Module API",
        default_version='v1',
        description="API for Odoo Module",
        terms_of_service="https://www.yourapp.com/terms/",
        contact=openapi.Contact(email="contact@yourapp.com"),
        license=openapi.License(name="Your License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)




urlpatterns = [
    # user
    path('api/user/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/user', UserRegistrationView.as_view(), name='user_register'),
    path('api/user/<int:pk>', UserEditView.as_view(), name='user_update'),

    # ruangan
    path('api/ruangan', RuanganListView.as_view(), name='ruangan_list'),
    path('api/ruangan/create', RuanganCreateView.as_view(), name='ruangan_create'),
    path('api/ruangan/detail/<uuid:pk>', RuanganDetailView.as_view(), name='ruangan_detail'),
    path('api/ruangan/<uuid:pk>', RuanganUpdateDeleteAPIView.as_view(), name='ruangan_update_delete'),

    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]





