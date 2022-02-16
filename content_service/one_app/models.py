from django.db import models


class Images(models.Model):
    image_url = models.CharField("Image URL", max_length=250)
    amount_show = models.CharField("Amount of show", max_length=250)
    categories = models.TextField("Categories")

    def __str__(self):
        return self.image_url

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'




