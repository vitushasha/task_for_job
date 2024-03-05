from django.db import models


class Author(models.Model):
    author_name = models.CharField(max_length=50)

    def str(self):
        return self.author_name

class Product(models.Model):
    author = models.ForeignKey(
                               Author,
                               on_delete=models.SET_NULL,
                               null=True,
                               related_name="products",
    )
    product_name = models.CharField(max_length=50)
    started = models.DateTimeField(default=None)
    cost = models.DecimalField(max_digits=8, decimal_places=2)
    min_student_amount = models.IntegerField()
    max_student_amount = models.IntegerField()

    def str(self):
        return self.product_name

class Lesson(models.Model):
    lesson_name = models.CharField(max_length=50)
    video_link = models.URLField()
    product = models.ForeignKey(
                                Product,
                                on_delete=models.CASCADE,
                                related_name="lessons",
    )

    def str(self):
        return self.lesson_name

class Student(models.Model):
    student_name = models.CharField(max_length=50)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="student")
    slug = models.SlugField()
    is_addmitted = models.BooleanField()

    def str(self):
        return self.student_name

class Group(models.Model):
    group_name = models.CharField(max_length=50)
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE,
                                related_name="groups")
    students = models.ManyToManyField(Student,
                                      related_name="students",
                                      blank=True)

    def str(self):
        return self.group_name
