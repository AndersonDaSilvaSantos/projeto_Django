from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=50)

    def__str__(self):
        return "{} ({})".format(self.nome)

class FormaPagamento(models.Model):
    nome = models.CharField(max_length=50)

     def__str__(self):
        return "{} ({})".format(self.nome)


class Conta(models.Model):
    descricao = models.CharField(max_length=150, verbose_name="Descrição")
    vencimento = models.DateField(max_length=50)
    valor = models.DoubleField(max_length=50)

    def__str__(self):
        return "{} ({})".format(self.nome, self.vencimento, self.valor)
