from rest_framework import generics
from .serializers import *
from .models import *


class articles(generics.ListAPIView):
    """
        Show Articles List
    """
    serializer_class = ArticlesSerialziers
    queryset = Articles.objects.all()




class articles_search(generics.ListAPIView):
    """
        Article search
        ?q=product title
    """
    serializer_class = ArticlesSerialziers

    def get_queryset(self):
        q = self.request.GET.get('q',False)
        return Articles.objects.filter(title__icontains=q).all()


class articles_filter_category(generics.ListAPIView):
    """
        Show Articles by category Id
    """
    serializer_class = ArticlesSerialziers

    def get_queryset(self):
        return Articles.objects.filter(category_id=self.kwargs['categoryID']).all()





class articles_detail(generics.ListAPIView):
    """
        Show Detail article
    """
    serializer_class = ArticlesSerialziers
    queryset = Articles.objects.all()
    lookup_field = 'id'





class categories(generics.ListAPIView):
    """
        Show Categories List
    """
    serializer_class = CategoriesSerialziers
    queryset = Categories.objects.all()





class category_detail(generics.ListAPIView):
    """
        Show Detail Category
    """
    serializer_class = CategoriesSerialziers
    queryset = Categories.objects.all()
    lookup_field = 'id'
