from rest_framework.generics import ListCreateAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Album
from .serializers import AlbumSerializer


class AlbumView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = AlbumSerializer
    pagination_class = PageNumberPagination

    def get_queryset(self):
        queryset = Album.objects.all()
        return self.paginate_queryset(queryset)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
