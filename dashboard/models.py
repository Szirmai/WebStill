from django.db import models

# Create your models here.


class Learn(models.Model):
    name = models.CharField(max_length=130)
    created = models.DateTimeField(auto_now_add=True, null=True)
    tutorials = models.TextField(max_length=10000)
    details = models.TextField(max_length=100000)
    
    def __str__(self):
        return str(self.name)
    
    class Meta:
        ordering = ['-created']