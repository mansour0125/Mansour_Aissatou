from django.contrib import admin
from .models import Produits

# Register your models here.
class AdminProduit(admin.ModelAdmin):
    list_display = ('nom','description','prix')
admin.site.register(Produits,AdminProduit)