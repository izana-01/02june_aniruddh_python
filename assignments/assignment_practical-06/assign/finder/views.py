from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework import status

from .models import Doctor
from .serializers import DoctorSerializer


# Create your views here.

@api_view(['GET', 'POST'])
def doctor_list(request):
    if request.method == 'GET':
        doctors = Doctor.objects.all()
        paginator = PageNumberPagination()
        paginator.page_size = 2
        page = paginator.paginate_queryset(doctors, request)
        serializer = DoctorSerializer(page, many=True)
        return paginator.get_paginated_response(serializer.data)

    if request.method == 'POST':
        serializer = DoctorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def doctor_detail(request, id):
    try:
        doctor = Doctor.objects.get(id=id)
    except Doctor.DoesNotExist:
        return Response({"error": "Doctor not found"}, status=404)

    if request.method == 'GET':
        return Response(DoctorSerializer(doctor).data)

    if request.method == 'PUT':
        serializer = DoctorSerializer(doctor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    if request.method == 'DELETE':
        doctor.delete()
        return Response({"message": "Doctor deleted"})
