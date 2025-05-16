from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    UpdateAPIView,
    DestroyAPIView,
)
from rest_framework.permissions import AllowAny

from .models import NatoMember
from .serializer import NatoMemberSerializer

class NatoMemberListAPIView(ListAPIView):
    # queryset = NatoMember.objects.all()
    serializer_class = NatoMemberSerializer

    def get_queryset(self):
        if 'keyword' in self.request.GET:
            queryset = NatoMember.objects.filter(name__icontains=self.request.GET['keyword'])
        else:
            queryset = NatoMember.objects.all()
        return queryset


class NatoMemberDetailAPIView(RetrieveAPIView):
    queryset = NatoMember.objects.all()
    serializer_class = NatoMemberSerializer
    lookup_field = 'slug'
    lookup_url_kwarg = 'name'

class NatoMemberCreateAPIView(CreateAPIView):
    queryset = NatoMember.objects.all()
    serializer_class = NatoMemberSerializer
    lookup_field = 'slug'
    permission_classes = (AllowAny,)

class NatoMemberUpdateAPIView(UpdateAPIView):
    queryset = NatoMember.objects.all()
    serializer_class = NatoMemberSerializer
    lookup_field = 'name'
    permission_classes = (AllowAny,)


class NatoMemberDestroyAPIView(DestroyAPIView):
    queryset = NatoMember.objects.all()
    serializer_class = NatoMemberSerializer
    lookup_field = 'slug'
    permission_classes = (AllowAny,)


