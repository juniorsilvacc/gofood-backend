from categories.models import Category
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from categories.forms import CategoryModelForm
from categories.serializers import CategorySerializer
from django.urls import reverse_lazy


class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get(self, request):
        categories = Category.objects.all()

        search = request.GET.get('search')
        if search:
            categories = Category.objects.filter(name__icontains=search)

        serializer = CategorySerializer(categories, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class CategoryRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


# Return template
class CategoryListView(ListView):
    model = Category
    template_name = 'categories/categories.html'
    context_object_name = 'categories'

    def get_queryset(self):
        categories = super().get_queryset().order_by('name')
        search = self.request.GET.get('name')
        if search:
            categories = categories.filter(name__icontains=search)
        return categories


class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryModelForm
    template_name = 'new_category.html'
    success_url = '/categories/'


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'categories/category_detail.html'


class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryModelForm
    template_name = 'category_update.html'

    def get_success_url(self):
        return reverse_lazy('category_detail', kwargs={'pk': self.object.pk})


class CategoryDeleteView(DeleteView):
    model = Category
    success_url = '/categories/'
