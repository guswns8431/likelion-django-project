from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()

    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:100]

class Portfolio(models.Model):
    title = models.CharField(max_length=255)
    image= models.ImageField(upload_t0='images/')
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.title