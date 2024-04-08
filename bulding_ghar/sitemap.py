# myproject/sitemap.py
from django.contrib.sitemaps import Sitemap
from app.sitemaps import ProjectSitemap, BlogPostSitemap

sitemaps = {
    'projects': ProjectSitemap,  # Key: Name you want to assign to this sitemap
    'blogposts': BlogPostSitemap,
}
