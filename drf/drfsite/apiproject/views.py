from django.shortcuts import render
from django.forms import model_to_dict
from rest_framework import generics, status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from .serializers import *
from .models import *
from .permissions import *
from .pagination import PostApiListPagination



class PostAPIList(generics.ListCreateAPIView):
    queryset = PostModel.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    pagination_class = PostApiListPagination


class PostAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = PostModel.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsOwnerOrReadOnly, )
    # представление авторизированным юзерам только через токен (JWT)
    # Активировать с искользованием сервиса ручного тестирования API
    # authentication_classes = (TokenAuthentication, )


class PostAPIDetailView(generics.RetrieveDestroyAPIView):
    queryset = PostModel.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAdminOrReadOnly, )
    # представление авторизированным юзерам только через токен (JWT)
    # Активировать с искользованием сервиса ручного тестирования API
    # authentication_classes = (TokenAuthentication, )


# class PostViewSet(viewsets.ModelViewSet):
#     # queryset = PostModel.objects.all()
#     serializer_class = PostSerializer

#     # переопределение queryset если нам нужно возвращать конкретные значения
#     def get_queryset(self):
#         pk = self.kwargs.get('pk')

#         if not pk:
#             return PostModel.objects.all()[:2]

#         return PostModel.objects.filter(pk=pk)

#     # detail=True - можно возвратить одну запись (по индексу в ссылке), иначе список
#     @action(methods=['get'], detail=True)
#     def category(self, request, pk):
#         cats = Category.objects.get(pk=pk)
#         return Response({'cats': cats.name})


# Для PostSerializer(serializers.Serializer)
# class PostAPIView(APIView):
#     def get(self, request):
#         p = PostModel.objects.all()
#         return Response({'posts': PostSerializer(p, many=True).data})
#         # True - значит сериализатр обрабатывает не одну запись, а несколько


#     def post(self, request):
#         serializer = PostSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({'post': serializer.data})


#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get('pk', None)
#         if not pk:
#             return Response({'error': 'Method PUT not allowed'})

#         try:
#             instance = PostModel.objects.get(pk=pk)
#         except:
#             return Response({'error': 'Object does not exists'})

#         serializer = PostSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({'post': serializer.data})


#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get('pk', None)
#         if not pk:
#             return Response({'error': 'Method DELETE not allowed'})
#         try:
#             obj = PostModel.objects.get(pk=pk)
#             obj.delete()
#         except:
#             return Response({'error': 'Object does not exists'})

#         return Response({"post": "delete post " + str(pk)})

# class PostAPIView(generics.ListAPIView):
#     queryset = PostModel.objects.all()
#     serializer_class = PostSerializer