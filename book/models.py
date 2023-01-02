from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone



class Book(models.Model):
    title = models.CharField(max_length= 30, null=False, blank=False)
    description = models.TextField()
    price = models.IntegerField()
    image = models.FileField(upload_to="books")
    created_on = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)



    def __str__(self):
        return self.title

    

    def get_absolute_url(self):
        return reverse("detail_book", kwargs ={"pk":self.pk})