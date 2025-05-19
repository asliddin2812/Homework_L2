from rest_framework import permissions, status
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    UpdateAPIView,
    DestroyAPIView,
)
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import NatoMember
from .serializer import NatoMemberSerializer
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

class NatoMemberListAPIView(ListAPIView):
    authentication_classes = (JWTAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['name','joined_year']
    search_fields = ['name']

    def get(self,request):
        members = NatoMember.objects.all().order_by('name')
        for backend in self.filter_backends:
            members = backend().filter_queryset(request, members,self)
        serializer = NatoMemberSerializer(members, many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = NatoMemberSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(created_by=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class NatoMemberDetailAPIView(RetrieveAPIView):
    queryset = NatoMember.objects.all()
    serializer_class = NatoMemberSerializer
    lookup_field = 'slug'

class NatoMemberCreateAPIView(CreateAPIView):
    queryset = NatoMember.objects.all()
    serializer_class = NatoMemberSerializer
    lookup_field = 'slug'
    permission_classes = (IsAuthenticated, IsAuthenticatedOrReadOnly )

class NatoMemberUpdateAPIView(UpdateAPIView):
    queryset = NatoMember.objects.all()
    serializer_class = NatoMemberSerializer
    lookup_field = 'name'
    permission_classes = (IsAuthenticated, IsAuthenticatedOrReadOnly)


class NatoMemberDestroyAPIView(DestroyAPIView):
    queryset = NatoMember.objects.all()
    serializer_class = NatoMemberSerializer
    lookup_field = 'slug'
    permission_classes = (IsAuthenticated,)


