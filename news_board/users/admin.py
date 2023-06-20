from django.contrib import admin

from users.models import FoxToken


# Register your models here.
@admin.register(FoxToken)
class FoxTokenAdmin(admin.ModelAdmin):
    list_display = ('key', 'user', )
    search_fields = ('user__username', )


