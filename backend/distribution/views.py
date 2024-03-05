from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import *
from .models import *
import json

"""Списки"""

class StudentList(APIView):

    def get(self, request, format=None):
        transformers = Student.objects.all()
        serializer = StudentSerializer(transformers, many=True)
        for student in Student.objects.filter(is_addmitted=True):
            groups = sorted(Group.objects.filter(product__product_name=student.product.product_name), key=lambda group: group.students.count())
            for group in groups:
                if group.students.count() < group.product.max_student_amount:
                    group.students.add(student)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data['student_name']
            subject = serializer.validated_data['products']
            is_addmitted = serializer.validated_data['is_addmitted']
            if len(Student.objects.filter(student_name=name, products=subject, is_addmitted=is_addmitted)) == 0:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductList(APIView):

    def get(self, request, format=None):
        transformers = Product.objects.all()
        serializer = ProductSerializer(transformers, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GroupList(APIView):

    def get(self, request, format=None):
        transformers = Group.objects.all()
        serializer = GroupSerializer(transformers, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = GroupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LessonList(APIView):

    def get(self, request, format=None):
        transformers = Lesson.objects.all()
        serializer = LessonSerializer(transformers, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = LessonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AuthorList(APIView):

    def get(self, request, format=None):
        transformers = Author.objects.all()
        serializer = AuthorSerializer(transformers, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ListProfuctsForStudent(APIView):

    def get(self, request, slug, format=None):
        data = Product.objects.filter(student__slug=slug, student__is_addmitted=True)
        serializer = ProductSerializer(data, many=True)
        return Response(serializer.data)

"""Детальная информация"""

class AuthorDetail(APIView):

    def get_object(self, pk):
        try:
            return Author.objects.get(pk=pk)
        except Author.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        transformer = self.get_object(pk)
        serializer = AuthorSerializer(transformer)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        transformer = self.get_object(pk)
        serializer = AuthorSerializer(transformer, data=request.data)
        if serializer.id_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        transformer = self.get_object(pk)
        serializer = AuthorSerializer(transformer,
                                      data=request.data,
                                      partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        transformer = self.get_object(pk)
        transformer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ProductDetail(APIView):

    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        transformer = self.get_object(pk)
        serializer = ProductSerializer(transformer)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        transformer = self.get_object(pk)
        serializer = ProductSerializer(transformer, data=request.data)
        if serializer.id_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        transformer = self.get_object(pk)
        serializer = ProductSerializer(transformer,
                                      data=request.data,
                                      partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        transformer = self.get_object(pk)
        transformer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class LessonDetail(APIView):

    def get_object(self, pk):
        try:
            return Lesson.objects.get(pk=pk)
        except Lesson.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        transformer = self.get_object(pk)
        serializer = LessonSerializer(transformer)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        transformer = self.get_object(pk)
        serializer = LessonSerializer(transformer, data=request.data)
        if serializer.id_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        transformer = self.get_object(pk)
        serializer = LessonSerializer(transformer,
                                      data=request.data,
                                      partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        transformer = self.get_object(pk)
        transformer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class GroupDetail(APIView):

    def get_object(self, pk):
        try:
            return Group.objects.get(pk=pk)
        except Group.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        transformer = self.get_object(pk)
        serializer = GroupSerializer(transformer)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        transformer = self.get_object(pk)
        serializer = GroupSerializer(transformer, data=request.data)
        if serializer.id_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        transformer = self.get_object(pk)
        serializer = GroupSerializer(transformer,
                                      data=request.data,
                                      partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        transformer = self.get_object(pk)
        transformer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class StudentDetail(APIView):

    def get_object(self, pk):
        try:
            return Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        transformer = self.get_object(pk)
        serializer = StudentSerializer(transformer)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        transformer = self.get_object(pk)
        serializer = StudentSerializer(transformer, data=request.data)
        if serializer.id_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        transformer = self.get_object(pk)
        serializer = StudentSerializer(transformer,
                                      data=request.data,
                                      partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        transformer = self.get_object(pk)
        transformer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)