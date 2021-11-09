import django_filters
from portal.models import Imovel


class ImovelFilterCondominio(django_filters.FilterSet):
    nomecondominio = django_filters.CharFilter(field_name='nomecondominio',lookup_expr='icontains')
    class Meta:
        model= Imovel
        fields= ['nomecondominio']

