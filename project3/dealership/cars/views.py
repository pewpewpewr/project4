from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema
from .models import Car
from .serializers import CarSerializer

class CarAPIView(APIView):
    @extend_schema(
        summary="List all cars",
        responses={200: CarSerializer(many=True)},
    )
    def get(self, request):
        cars = Car.objects.all()
        serializer = CarSerializer(cars, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(
        summary="Create a new car",
        request=CarSerializer,
        responses={201: CarSerializer},
    )
    def post(self, request):
        serializer = CarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(
        summary="Update a car",
        request=CarSerializer,
        responses={200: CarSerializer},
    )
    def put(self, request, pk):
        try:
            car = Car.objects.get(pk=pk)
        except Car.DoesNotExist:
            return Response({"error": "Car not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = CarSerializer(car, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(
        summary="Partially update a car",
        request=CarSerializer,
        responses={200: CarSerializer},
    )
    def patch(self, request, pk):
        try:
            car = Car.objects.get(pk=pk)
        except Car.DoesNotExist:
            return Response({"error": "Car not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = CarSerializer(car, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(
        summary="Delete a car",
        responses={204: "No Content"},
    )
    def delete(self, request, pk):
        try:
            car = Car.objects.get(pk=pk)
            car.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Car.DoesNotExist:
            return Response({"error": "Car not found"}, status=status.HTTP_404_NOT_FOUND)
