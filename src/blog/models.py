from django.db import models

class Blogs(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    description = models.TextField()
    url = models.URLField(blank=True)  # blank - не обязательно для заполнения

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Blogs'