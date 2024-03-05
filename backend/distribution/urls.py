from django.urls import path
from .views import *

urlpatterns = [
    path('students/<slug:slug>/', ListProfuctsForStudent.as_view()),
    path('students/<int:pk>/', StudentDetail.as_view(), name='student_detail'),
    path('authors/<int:pk>/', AuthorDetail.as_view(), name='author_detail'),
    path('products/<int:pk>/', ProductDetail.as_view(), name='product_detail'),
    path('lessons/<int:pk>/', LessonDetail.as_view(), name='lesson_detail'),
    path('groups/<int:pk>/', GroupDetail.as_view(), name='group_detail'),
    path('students/', StudentList.as_view(), name='student_list'),
    path('products/', ProductList.as_view(), name='product_list'),
    path('lessons/', LessonList.as_view(), name='lesson_list'),
    path('groups/', GroupList.as_view(), name='group_list'),
    path('authors/', AuthorList.as_view(), name='author_list'),
]