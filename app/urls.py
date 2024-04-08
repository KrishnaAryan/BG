
from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

from django.contrib.sitemaps.views import sitemap

from django.contrib.sitemaps import Sitemap
from app.sitemaps import *

sitemaps = {
    'projects': ProjectSitemap,  # Key: Name you want to assign to this sitemap
    'blogposts': BlogPostSitemap,
    'index': IndexSitemap,
    'other_urls': OtherUrlsSitemap,
}
urlpatterns = [
    path('', views.new_landing_page, name='new_landing_page'),
    path('index', views.index, name='index'),
    path('project_view/<int:id>/', views.project_view, name='project_view'),
    path('design_image/<int:id>/', views.design_image, name='design_image'),
    # path('architecture', views.architecture, name='architecture'),
    # path('construction', views.construction, name='construction'),
    path('house_villa', views.house_villa, name='house_villa'),
    path('custom_project', views.custom_project, name='custom_project'),
    path('renovation', views.renovation, name='renovation'),
    path('floor_addition', views.floor_addition, name='floor_addition'),
    
    path('packages', views.packages, name='packages'),
    
    path('submit-leads/', views.submit_leads, name='submit_leads'),
    path('pdf_download', views.pdf_download, name='pdf_download'),

    
    path('structure', views.structure, name='structure'),
    path('kitchen', views.kitchen, name='kitchen'),
    path('bathroom', views.bathroom, name='bathroom'),
    path('woodwork', views.woodwork, name='woodwork'),
    path('painting', views.painting, name='painting'),
    path('flooring', views.flooring, name='flooring'),
    path('electrical', views.electrical, name='electrical'),
    path('watertanks', views.watertanks, name='watertanks'),
    path('others', views.others, name='others'),
    path('exclusions', views.exclusions, name='exclusions'),
    path('upgrades', views.upgrades, name='upgrades'),
    path('warranty', views.warranty, name='warranty'),
    path('note', views.note, name='note'),
    path('architecture_portfolio', views.architecture_portfolio, name='architecture_portfolio'),
    path('architecture_portfolio_view/<int:id>/', views.architecture_portfolio_view, name='architecture_portfolio_view'),
    path('construction_project', views.construction_project, name='construction_project'),
    path('construction_project_view/<int:id>/', views.construction_project_view, name='construction_project_view'),
    path('architecture_portfolio_viewdesign_image/<int:id>/', views.architecture_portfolio_viewdesign_image, name='architecture_portfolio_viewdesign_image'),
    path('about',views.about, name='about'),
    path('career',views.career, name='career'),
    path('contactus',views.contactus, name='contactus'),
    path('popup/', views.popup, name='popup'),

    path('calculator/',views.calculator, name='calculator'),
    path('package/<int:id>/', views.package_details_view, name='package_details'),
    path('video',views.video, name='video'),
    path('category_video/<int:id>',views.category_video, name='category_video'),
    path('landing_page',views.landing_page, name='landing_page'),
    
    path('blogs', views.blogs, name='blogs'),
    # path('blogs/<int:post_id>/', views.blogs_details, name='blog_details'),
    path('blogs/<slug:slug>/', views.blogs_details, name='blog_details'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),

    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# {% url 'package_details' id=1 %}

