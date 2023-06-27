from django.shortcuts import render, HttpResponse

# Create your views here.

from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework.response import Response
from .models import Book, Publish, Author
from rest_framework.generics import GenericAPIView

# 针对模型设计序列化器,如下面针对Book做
# class BookSerializers(serializers.Serializer):
#     title = serializers.CharField(max_length=32)
#     price = serializers.IntegerField()
#     date = serializers.DateField(source='pub_date') #source的值需与序列化时的键相同
#
#     def create(self, validated_data):
#         new_book = Book.objects.create(**self.validated_data)
#         return new_book
#
#
#     def update(self, instance, validated_data):
#         Book.objects.filter(pk=instance.pk).update(**validated_data)
#         updated_book = Book.objects.get(pk=id)
#         return updated_book

#
# class BookSerializers(serializers.ModelSerializer):
#     date = serializers.DateField(source='pub_date')
#
#     class Meta:
#         model = Book
#         # fields = '__all__'  # ['title', 'price', ] #'__all__'
#         exclude = ['pub_date']


# class BookView(APIView):
#
#     def get(self, request):
#         # 获取所有书籍
#         book_list = Book.objects.all()  # queryset[book01,book02,...]
#         # 构建序列化器对象
#         serializer = BookSerializers(instance=book_list, many=True)  # 如果是单个数据，many=False
#
#         return Response(serializer.data)
#
#     def post(self, request):
#
#         # 构建序列化对象
#         serializer = BookSerializers(data=request.data)
#         if serializer.is_valid():
#             # 通过校验的数据插入数据库
#             # new_book = Book.objects.create(**serializer.validated_data)
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
#
#
# class BookDetailView(APIView):
#
#     def get(self, request, id):
#         # print('data: ', request.data)
#         book = Book.objects.get(pk=id)
#         serializer = BookSerializers(instance=book, many=False)
#         return Response(serializer.data)
#
#     def put(self, request, id):
#         print('data: ', request.data)
#         # return Response()
#         update_book = Book.objects.get(pk=id)
#         serializer = BookSerializers(instance=update_book, data=request.data)
#         if serializer.is_valid():
#             # Book.objects.filter(pk=id).update(**serializer.validated_data)
#             # updated_book = Book.objects.get(pk=id)
#             # serializer.instance = updated_book
#             serializer.save()
#
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
#
#     def delete(self, request, id):
#         Book.objects.filter(pk=id).delete()
#         return Response()


# Chapter 1 --------------------------------基于APIView的接口实现-------------------------------------


# Chapter 2 -----------------------------------基于genericAPIView的接口实现---------------------------------

# class BookSerializers(serializers.ModelSerializer):
#     # date = serializers.DateField(source='pub_date')
#
#     class Meta:
#         model = Book
#         fields = '__all__'
#
#
# class BookView(GenericAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializers
#
#     def get(self, request):
#         # serializer = BookSerializers(instance=self.queryset(), many=True)
#         serializer = self.get_serializer_class()(instance=self.get_queryset(), many=True)
#         return Response(serializer.data)
#
#     def post(self, request,):
#         serializer = self.get_serializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
#
#
# class BookDetailView(GenericAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializers
#
#     def get(self,request,pk):
#         serializer = self.get_serializer(instance=self.get_object(), many=False)
#         return Response(serializer.data)
#
#     def put(self,request, pk):
#         print('data: ', request.data)
#         # return Response()
#
#         serializer = self.get_serializer(instance=self.get_object(), data=request.data)
#         if serializer.is_valid():
#             # Book.objects.filter(pk=id).update(**serializer.validated_data)
#             # updated_book = Book.objects.get(pk=id)
#             # serializer.instance = updated_book
#             serializer.save()
#
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
#
#     def delete(self,request, pk):
#         self.get_object().delete()
#         return Response()
#
# # ------------------------ Publish ----------------------------------------
#
# class PublishSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = Publish
#         fields = '__all__'
#
#
# class PublishView(GenericAPIView):
#
#     def get(self, request):
#         # 获取所有书籍
#         publish_list = Publish.objects.all()  # queryset[book01,book02,...]
#         # 构建序列化器对象
#         serializer = PublishSerializers(instance=publish_list, many=True)  # 如果是单个数据，many=False
#
#         return Response(serializer.data)
#
#     def post(self, request):
#
#         # 构建序列化对象
#         serializer = PublishSerializers(data=request.data)
#         if serializer.is_valid():
#             # 通过校验的数据插入数据库
#             # new_book = Book.objects.create(**serializer.validated_data)
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
#
#
# class PublishDetailView(GenericAPIView):
#
#     def get(self, request, id):
#         print('data: ', request.data)
#         publish = Publish.objects.get(pk=id)
#         serializer = PublishSerializers(instance=publish, many=False)
#         return Response(serializer.data)
#
#     def put(self, request, id):
#         print('data: ', request.data)
#         # return Response()
#         update_publish = Publish.objects.get(pk=id)
#         serializer = PublishSerializers(instance=update_publish, data=request.data)
#         if serializer.is_valid():
#             # Book.objects.filter(pk=id).update(**serializer.validated_data)
#             # updated_book = Book.objects.get(pk=id)
#             # serializer.instance = updated_book
#             serializer.save()
#
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
#
#     def delete(self, request, id):
#         Publish.objects.filter(pk=id).delete()
#         return Response()
#
# # -------------------------------Author--------------------------------------------
#
# class AuthorSerializers(serializers.ModelSerializer):
#     # date = serializers.DateField(source='pub_date')
#
#     class Meta:
#         model = Author
#         fields = '__all__'
#
#
# class AuthorView(GenericAPIView):
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializers
#
#     def get(self, request):
#         # serializer = BookSerializers(instance=self.queryset(), many=True)
#         serializer = self.get_serializer(instance=self.get_queryset(), many=True)
#         return Response(serializer.data)
#
#     def post(self, request,):
#         serializer = self.get_serializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
#
#
# class AuthorDetailView(GenericAPIView):
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializers
#
#     def get(self,request,pk):
#         serializer = self.get_serializer(instance=self.get_object(), many=False)
#         return Response(serializer.data)
#
#     def put(self,request, pk):
#         print('data: ', request.data)
#         # return Response()
#
#         serializer = self.get_serializer()(instance=self.get_object(), data=request.data)
#         if serializer.is_valid():
#             # Book.objects.filter(pk=id).update(**serializer.validated_data)
#             # updated_book = Book.objects.get(pk=id)
#             # serializer.instance = updated_book
#             serializer.save()
#
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
#
#     def delete(self,request, pk):
#         self.get_object().delete()
#         return Response()


# -------------------------------基于Minxin混合类的接口实现--------------------------------------------
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, \
    RetrieveModelMixin, DestroyModelMixin, UpdateModelMixin


class BookSerializers(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class BookView(ListModelMixin, CreateModelMixin, GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


class BookDetailView(UpdateModelMixin, RetrieveModelMixin, DestroyModelMixin, GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers

    def get(self, request, pk):
        return self.retrieve(request, pk)

    def put(self, request, pk):
        return self.update(request, pk)

    def delete(self, request, pk):
        return self.destroy(request, pk)


# --------------------------------第四版接口设计（再封装）----------------------------------
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


class PublishSerializers(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Publish


class PublishView(ListCreateAPIView):
    queryset = Publish.objects.all()
    serializer_class = PublishSerializers


class PublishDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Publish.objects.all()
    serializer_class = PublishSerializers


# -------------------------------------ViewSet类,重建分发机制----------------------------------

from rest_framework.viewsets import ViewSet
from rest_framework.mixins import ListModelMixin, \
    CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin


class AuthorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


#
# class AuthorView(GenericAPIView):
#     def get_all(self, request):
#         return Response('Get all info')
#
#     def add_one(self, request):
#         return Response('Add one more')
#
#     def get_one(self, request, pk):
#         return Response("Get one's info")
#
#     def update(self, request, pk):
#         return Response('Update one obj')
#
#     def delete_one(self, request, pk):
#         return Response('Delete one obj')
#


# ---------------------------------------Final version---------------------------------------
from rest_framework.viewsets import ModelViewSet


class AuthorView(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializers
