from django.db import models

class Phone(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.CharField(max_length=256)
    release_date = models.DateField(auto_now_add=True)
    lte_exists = models.BooleanField(default=False)
    slug = models.SlugField(max_length = 50)

    def __str__(self):
        return  str(self.id) + ' | ' + self.name + ' | ' + self.price + ' | ' \
               + self.image + ' | ' + str(self.release_date) + ' | ' \
               + self.lte_exists + ' | ' + self.slug

