from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import generics,status
from .serializers import *
from .models import *



class products(generics.ListAPIView):
    """
        Show Products List
    """
    serializer_class = ProductsSerialziers
    queryset = Products.objects.filter(inventory__gt=0).all()




class products_search(generics.ListAPIView):
    """
        Product search
        ?q=product title
    """
    serializer_class = ProductsSerialziers

    def get_queryset(self):
        q = self.request.GET.get('q',False)
        return Products.objects.filter(title__icontains=q, inventory__gt=0).all()


class products_filter_category(generics.ListAPIView):
    """
        Show products by category Id
    """
    serializer_class = ProductsSerialziers

    def get_queryset(self):
        return Products.objects.filter(category_id=self.kwargs['categoryID'],inventory__gt=0).all()



class product_detail(generics.ListAPIView):
    """
        Show Detail Product
    """
    serializer_class = ProductsSerialziers
    queryset = Products.objects.filter(inventory__gt=0).all()
    lookup_field = 'id'





class product_comments(generics.ListAPIView):
    """
        Show Comments List
    """

    serializer_class = CommentsSerialziers
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Comments.objects.filter(product_id=self.kwargs['id'],status=True).all()


class product_comment_create(generics.CreateAPIView):
    """
        Create a comment
    """
    serializer_class = CommentsSerialziers
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        data = CommentsSerialziers(data=self.request.data)
        if data.is_valid():
            id = self.kwargs['id']
            product = Products.objects.filter(id=id).first()
            if product is not None:
                comment = Comments.objects.filter(user_id=self.request.id,product_id=id).first()
                if comment is not None:
                    return Response({'message': 'کاربر قبلا کامنت ثبت کرده است'},status=status.HTTP_400_BAD_REQUEST)
                else:
                    comment = Comments.objects.filter(id=data.instance.id).first()
                    comment.user_id = self.request.id
                    comment.product_id = id
                    comment.save()
                    return Response({'message': 'با موفقیت اضافه شد پس از تایید نمایش داده خواهد شد'})
            else:
                return Response({'message': 'محصول وجود ندارد'},status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(data.errors)


class product_likes(generics.ListAPIView):
    serializer_class = LikesSerialziers

    def get(self, request, *args, **kwargs):
        return Response({'count': Likes.objects.filter(product_id=self.kwargs['id'],status=True).count()})


class product_dislikes(generics.ListAPIView):
    serializer_class = LikesSerialziers

    def get(self, request, *args, **kwargs):
        return Response({'count': Likes.objects.filter(product_id=self.kwargs['id'],status=False).count()})


class product_like_create(generics.CreateAPIView):
    """
        Create a like for product
    """
    serializer_class = LikesSerialziers
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        data = LikesSerialziers(data=self.request.data)
        if data.is_valid():
            id = self.kwargs['id']
            product = Products.objects.filter(id=id).first()
            if product is not None:
                like = Likes.objects.filter(user_id=self.request.id,product_id=id).first()
                if like is not None:
                    return Response({'message': 'کاربر قبلا لایک ثبت کرده است'},status=status.HTTP_400_BAD_REQUEST)
                else:
                    like = Likes.objects.filter(id=data.instance.id).first()
                    like.user_id = self.request.id
                    like.product_id = id
                    like.save()
                    return Response({'message': 'با موفقیت اضافه شد'})
            else:
                return Response({'message': 'محصول وجود ندارد'},status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(data.errors)



class products_sliders(generics.ListAPIView):
    """
        Show Sliders List
    """
    serializer_class = SlidersSerialziers
    queryset = Sliders.objects.all()


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







class carts(generics.ListAPIView):
    """
        Show Orders List in cart
    """
    serializer_class = OrdersSerializers
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Orders.objects.filter(cart__customer_id=self.request.user.id,payment_status=False).all()






class cart_create(generics.CreateAPIView):
    """
        Create Order in cart
    """
    serializer_class = OrdersSerializers
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        data = OrdersSerializers(data=self.request.data)
        if data.is_valid():
            product = Products.objects.filter(id=self.kwargs['id']).first()
            if product.inventory >= int(self.request.data['count']):
                if product is not None:
                    cart = Carts.objects.filter(customer_id=self.request.user.id,payment_status=False).first()
                    if cart is None:
                        Carts.objects.create(customer_id=self.request.user.id,payment_status=False)
                    else: pass
                    cart = Carts.objects.filter(customer_id=self.request.user.id,payment_status=False).first()
                    Orders.objects.create(cart_id=cart.id,product_id=self.kwargs['id'],title=product.title,descriptions=product.descriptions,price=product.price,count=self.request.data['count'])
                    return Response({'message': 'محصول به سبد خرید اضافه شد'})
                else:
                    return Response({'message': 'محصول وجود ندارد'},status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'message': 'ERROR'},status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(data.errors)



class cart_delete(generics.DestroyAPIView):
    """
        Delete Order in cart
    """
    serializer_class = OrdersSerializers
    permission_classes = [IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        order = Orders.objects.filter(id=self.kwargs['id'],cart__customer_id=self.request.user.id,payment_status=False).first()
        if order is not None:
            order.delete()
            return Response({'message': 'حذف شد'})
        else:
            return Response({'message': 'محصول وجود ندارد'},status=status.HTTP_400_BAD_REQUEST)






class tracking(generics.ListAPIView):
    """
        Product tracking with tracking code
    """
    serializer_class = TrackingsSerializers

    def get_queryset(self):
        return [Trackings.objects.filter(code=self.kwargs['code']).first()]

