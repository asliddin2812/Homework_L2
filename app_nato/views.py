# from rest_framework import permissions, status
# from rest_framework.generics import (
#     ListAPIView,
#     RetrieveAPIView,
#     CreateAPIView,
#     UpdateAPIView,
#     DestroyAPIView,
# )
# from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly, IsAuthenticated
# from rest_framework.response import Response
# from rest_framework_simplejwt.authentication import JWTAuthentication
#
# from .models import NatoMember
# from .serializer import NatoMemberSerializer
# from rest_framework.filters import SearchFilter
# from django_filters.rest_framework import DjangoFilterBackend
#
# class NatoMemberListAPIView(ListAPIView):
#     authentication_classes = (JWTAuthentication,)
#     permission_classes = (permissions.IsAuthenticated,)
#     filter_backends = [DjangoFilterBackend, SearchFilter]
#     filterset_fields = ['name','joined_year']
#     search_fields = ['name']
#
#     def get(self,request):
#         members = NatoMember.objects.all().order_by('name')
#         for backend in self.filter_backends:
#             members = backend().filter_queryset(request, members,self)
#         serializer = NatoMemberSerializer(members, many=True)
#         return Response(serializer.data)
#
#     def post(self,request):
#         serializer = NatoMemberSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save(created_by=self.request.user)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# class NatoMemberDetailAPIView(RetrieveAPIView):
#     queryset = NatoMember.objects.all()
#     serializer_class = NatoMemberSerializer
#     lookup_field = 'slug'
#
# class NatoMemberCreateAPIView(CreateAPIView):
#     queryset = NatoMember.objects.all()
#     serializer_class = NatoMemberSerializer
#     lookup_field = 'slug'
#     permission_classes = (IsAuthenticated, IsAuthenticatedOrReadOnly )
#
# class NatoMemberUpdateAPIView(UpdateAPIView):
#     queryset = NatoMember.objects.all()
#     serializer_class = NatoMemberSerializer
#     lookup_field = 'name'
#     permission_classes = (IsAuthenticated, IsAuthenticatedOrReadOnly)
#
#
# class NatoMemberDestroyAPIView(DestroyAPIView):
#     queryset = NatoMember.objects.all()
#     serializer_class = NatoMemberSerializer
#     lookup_field = 'slug'
#     permission_classes = (IsAuthenticated,)
#
#
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response

from .serializer import NatoMemberListSerializer,NatoMemberSerializer
from .models import NatoMember

class NatoMemberViewSet(viewsets.ModelViewSet):
    queryset = NatoMember.objects.all()
    lookup_field = 'slug'
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_serializer_class(self):
        if self.action == 'list':
            return NatoMemberListSerializer
        return NatoMemberSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            name = request.data.get('name')
            if not name or len(name) < 3:
                return Response(
                    {"Xato!": "Name uzunligi 3 dan katta bolishi kerak!"},
                    status=status.HTTP_400_BAD_REQUEST
                )
            continent = request.data.get('continent')
            valid_continents = ['Europe', 'North America', 'Asia']
            if continent not in valid_continents:
                return Response(
                    {"error": f"Continentni to'g'ri kiriting!: {', '.join(valid_continents)}."},
                    status=status.HTTP_400_BAD_REQUEST
                )
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.joined_year.year > 2025:
            return Response(
                {"Xato": "Members jadvali 2025 dan keyngi davlatlar o'chirildi!."},
                status=status.HTTP_403_FORBIDDEN
            )
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)