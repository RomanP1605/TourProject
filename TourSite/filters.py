# from django_filters import FilterSet, CharFilter, NumberFilter
# from django.forms import HiddenInput
#
# from .models import Product
#
#
# class ProductFilter(FilterSet):
#     price_max = NumberFilter(field_name="price", lookup_expr="lte")
#     price_min = NumberFilter(field_name="price", lookup_expr="gte")
#     category = CharFilter(
#         field_name="category__name", lookup_expr="exact", widget=HiddenInput()
#     )
#
#     class Meta:
#         model = Product
#         fields = []
