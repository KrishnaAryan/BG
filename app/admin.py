from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Baner)



class ConstructionImageInline(admin.TabularInline):
    model = ConstructionImage
    extra = 1

class DesignImageInline(admin.TabularInline):
    model = DesignImage
    extra = 1

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('project_id', 'location', 'client_name', 'area', 'floor', 'package', 'status')
    search_fields = ('project_id', 'location', 'client_name')
    inlines = [
        ConstructionImageInline,
        DesignImageInline,
    ]
    
# admin.site.register(Package)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'mobile', 'email', 'location')
    search_fields = ('name', 'email', 'location')
    list_filter = ('location',)
    list_per_page = 20
    

@admin.register(Offerbaner)
class OfferbanerAdmin(admin.ModelAdmin):
    list_display = ['id', 'image']
    list_display_links = ['id', 'image']   
    
admin.site.register(Youtuble)





@admin.register(PackageName)
class PackageNameAdmin(admin.ModelAdmin):
    list_display = ('id','name',)
    search_fields = ('id','name',)

@admin.register(PackageDetails)
class PackageDetailsAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'package_detail')
    list_filter = ('id','name',)
    search_fields = ('id','name__name', 'package_detail')

    def name(self, obj):
        return obj.name.name

admin.site.site_header = 'Your Admin Site'
admin.site.site_title = 'Your Admin Site'



class YoutubeURLInline(admin.TabularInline):
    model = YoutubeURL

class YoutubeCategoryAdmin(admin.ModelAdmin):
    inlines = [YoutubeURLInline]

admin.site.register(YoutubeCategory, YoutubeCategoryAdmin)


admin.site.site_header="Building Ghar"



admin.site.register(BlogPost)


from django.contrib import admin
from .models import Leads, PackagePDF

@admin.register(Leads)
class LeadsAdmin(admin.ModelAdmin):
    list_display = ('name', 'mobile', 'email')
    list_filter = ('name', 'mobile')
    search_fields = ('name', 'mobile')

@admin.register(PackagePDF)
class PackagePDFAdmin(admin.ModelAdmin):
    list_display = ('id','upload_pdf',)
