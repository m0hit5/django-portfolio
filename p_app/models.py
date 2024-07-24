from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technologies = models.CharField(max_length=200)
    image = models.ImageField(upload_to='projects/')
    github_link = models.URLField()
    live_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title

class Contact(models.Model):
    name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100, blank=True)
    designation = models.CharField(max_length=100, blank=True)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name
