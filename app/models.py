from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class Baner(models.Model):
    image=models.ImageField(upload_to='images/baner')
    
class BanerMobile(models.Model):
    image=models.ImageField(upload_to='images/baner')
    
    

from django.db import models
from django.urls import reverse

class Project(models.Model):
    feature_image = models.ImageField(upload_to='images/project')
    project_id = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    client_name = models.CharField(max_length=50)
    area = models.CharField(max_length=50)
    floor = models.CharField(max_length=50)
    package = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)  # Add this line

    def get_absolute_url(self):
        return reverse('project_detail', args=[self.pk])

class ConstructionImage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    image=models.ImageField(upload_to='images/ProjectImage')
    
    
class DesignImage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    image=models.ImageField(upload_to='images/ProjectImage')
    
class Package(models.Model):
    Package=RichTextField()
    
    

class Leads(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)
    
class PackagePDF(models.Model):
    upload_pdf=models.FileField(upload_to='PackagePDF/')

    
    from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=20)
    email = models.EmailField()
    location = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name
    
    
    
class Offerbaner(models.Model):
    image=models.ImageField(upload_to='images/Offer Baner')
    
    
class Youtuble(models.Model):
    url=models.TextField(max_length=2000)
    
    
class PackageName(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
class PackageDetails(models.Model):
    name=models.ForeignKey(PackageName, on_delete=models.CASCADE)
    package_detail=RichTextField()
    def __str__(self):
        return self.package_detail


    
class YoutubeCategory(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
class YoutubeURL(models.Model):
    category = models.ForeignKey(YoutubeCategory, on_delete=models.CASCADE)
    url = models.CharField(max_length=500)
    
    
    

# class BlogPost(models.Model):
#     image=models.ImageField(upload_to='blog/image', blank=True, null=True)
#     title = models.CharField(max_length=200)
#     content_sort= models.CharField(max_length=200)
#     content = RichTextField()
#     date = models.DateTimeField()
#     author = models.CharField(max_length=100)
#     click_count = models.IntegerField(default=0)

#     def __str__(self):
#         return self.title


# from ckeditor.fields import RichTextField

from django.utils.text import slugify

class BlogPost(models.Model):
    image = models.ImageField(upload_to='blog/image', blank=True, null=True)
    title = models.CharField(max_length=200)
    content_sort = models.CharField(max_length=200)
    content = RichTextField()
    date = models.DateTimeField()
    author = models.CharField(max_length=100)
    click_count = models.IntegerField(default=0)
    slug = models.SlugField(unique=True, max_length=200, null=True, blank=True)

    def save(self, *args, **kwargs):
        # Generate slug automatically if not provided
        if not self.slug:
            self.slug = slugify(self.title.replace(" ", "-"))  # Replace spaces with hyphens
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blogpost_detail', args=[self.id])
