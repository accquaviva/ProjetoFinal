from django.contrib import admin
from .models import *


class MovRotativoAdm(admin.ModelAdmin):
    list_display = (
        'checkin','checkout','valor_hora','pago','total','horasTotal','veiculo')

    def veiculo(self,obj):
        return obj.veiculo

class MovMensalistaAdm(admin.ModelAdmin):
    list_display = (
        'mensalista','dt_pgto','total'
    )

admin.site.register(Marca)
admin.site.register(Veiculo)
admin.site.register(Pessoa)
admin.site.register(Parametros)
admin.site.register(MovRotativo,MovRotativoAdm)
admin.site.register(Mensalista)
admin.site.register(MovMensalista,MovMensalistaAdm)