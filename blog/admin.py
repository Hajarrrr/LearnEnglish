from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *    #,Images

# Register your models here.

#admin.site.register(Images)


@admin.register(nouns)
class nounsAdmin(ImportExportModelAdmin):
    pass

@admin.register(verbs)
class verbssAdmin(ImportExportModelAdmin):
    pass

@admin.register(cross)
class crossAdmin(ImportExportModelAdmin):
    pass
