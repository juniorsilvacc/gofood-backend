from categories.models import Category
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from categories.serializers import CategorySerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from drf_spectacular.utils import extend_schema


@extend_schema(tags=["Categories"])
class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get(self, request):
        print("Usuário autenticado:", request.user.is_authenticated)
        print("Usuário:", request.user)
        
        categories = Category.objects.all()

        search = request.GET.get('search')
        if search:
            categories = Category.objects.filter(name__icontains=search)

        serializer = CategorySerializer(categories, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsAuthenticated()]
        return [AllowAny()]


@extend_schema(tags=["Categories"])
class CategoryRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
