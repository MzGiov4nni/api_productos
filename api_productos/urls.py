from django.urls import path
from api_productos import views

urlpatterns=[

    path('', views.Listar_producto, name="Pruductos"),
    path('detalle/<str:pk>', views.Detalle_producto, name="Detalles_producto"),
    path('crear', views.Registro_producto, name="Registar_producto"),
    path('actualizar/<str:pk>/', views.Actualizar_producto, name="Actualizar_producto"),
    path('eliminar/<str:pk>/', views.Eliminar_producto, name="Eliminar_prducto"),
]