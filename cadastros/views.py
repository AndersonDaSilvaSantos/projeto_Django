from django.views.generic.edit import CreateView

from.models import Conta, FormaPagamento,Categoria

# Create your views here.
from django.urls import reverse_lazy

class CampoCreate(CreateView);
    model = Campo
    fields = ['nome', 'Usuario']