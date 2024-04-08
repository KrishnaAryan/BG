# In myapp/sitemaps.py
from django.urls import reverse
from django.contrib.sitemaps import Sitemap
from .models import Project, BlogPost

class ProjectSitemap(Sitemap):
    changefreq = 'daily'  # How often the content changes (e.g., hourly, daily, weekly, monthly)
    priority = 0.8  # The priority of the content relative to other URLs on your site (0.0 to 1.0)

    def items(self):
        return Project.objects.all()  # Queryset of objects to include in the sitemap

    def lastmod(self, obj):
        return obj.date_created  # Assuming 'date_created' is the attribute in your Project model indicating creation time

    def location(self, obj):
        return reverse('project_view', args=[obj.id])  # Assuming 'project_view' is the name of your view function for project detail

from django.urls import reverse
from django.contrib.sitemaps import Sitemap
from .models import BlogPost

class BlogPostSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.9

    def items(self):
        return BlogPost.objects.all()

    def lastmod(self, obj):
        return obj.date

    def location(self, obj):
        return reverse('blog_details', args=[obj.slug])


class IndexSitemap(Sitemap):
    changefreq = 'daily'
    priority = 1.0

    def items(self):
        return ['index']  # Name of the index view

    def location(self, item):
        return reverse(item)

class OtherUrlsSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.5

    def items(self):
        return [
            'house_villa', 'custom_project', 'renovation', 'floor_addition',
            'packages',
            'architecture_portfolio', 'construction_project',
            'about', 'career', 'contactus',
            'landing_page'
        ]  # List of view names

    def location(self, item):
        return reverse(item)