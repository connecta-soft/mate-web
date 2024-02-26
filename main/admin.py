from django.contrib import admin
from .models import City, States, Leads, Applications, Leads2

# Register your models here.


admin.site.register(City)
admin.site.register(States)
admin.site.register(Applications)


class LeadsAdmin(admin.ModelAdmin):
    list_display = [it.name for it in Leads._meta.fields]

    class Meta:
        models = Leads


admin.site.register(Leads, LeadsAdmin)

class LeadsAdmin2(admin.ModelAdmin):
    list_display = [it.name for it in Leads._meta.fields]

    class Meta:
        models = Leads2


admin.site.register(Leads2, LeadsAdmin2)