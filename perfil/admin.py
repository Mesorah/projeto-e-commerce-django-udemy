from django.contrib import admin

from perfil import models


@admin.register(models.Perfil)
class PerfilAdmin(admin.ModelAdmin):
    pass
