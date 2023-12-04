# Create your views here.
from .serializer import Productos_Serializer
from .models import producto
from rest_framework.decorators import api_view
from django.shortcuts import render
from rest_framework.response import Response

@api_view(['GET'])
def Listar_producto(request):
    productos = producto.objects.all()
    serializer = Productos_Serializer(productos, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def Detalle_producto(request, pk):
    productos = producto.objects.get(id=pk)
    serializer = Productos_Serializer(productos, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def Registro_producto(request):
    serializer = Productos_Serializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response(serializer.errors)

    return Response(serializer.data)


@api_view(['PUT'])
def Actualizar_producto(request, pk):
    productos = producto.objects.get(id=pk)
    serializer = Productos_Serializer(instance=producto, data=request.data)

    if serializer.is_valid():
        serializer.save()
    else:
        return Response(serializer.errors)
    return Response(serializer.data)


@api_view(['DELETE'])
def Eliminar_producto(request, pk):
    productos = producto.objects.get(id=pk)
    productos.delete()

    return Response('Eliminado')

