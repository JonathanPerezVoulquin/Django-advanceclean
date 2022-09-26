from django.contrib import admin

from clients.models import ListaDeClientes, agregar
# Register your models here.
class Client(admin.ModelAdmin):
    list_display = ('id', 'nombre_apellido', 'direccion', 'telefono','ultimo_lavado','precio','detalle','email')
    class Meta:
        managed = False
        db_table = 'lista_de_clientes_'
class Add(admin.ModelAdmin):
	list_display = ('first_name', 'last_name')

	class Meta:
		db_table= 'agregar'


admin.site.register(ListaDeClientes,Client)
admin.site.register(agregar, Add)

