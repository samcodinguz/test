from django.db import models

# Create your models here.
class New(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    img = models.ImageField(upload_to='news/', blank=True, null=True)

    def __str__(self):
        return self.title