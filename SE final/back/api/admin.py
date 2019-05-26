from django.contrib import admin
from api.models import Competition,Members

admin.site.register(Members)
@admin.register(Competition)
class CompetitionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', )

# Register your models here.
