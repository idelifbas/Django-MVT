from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Category(models.Model):
    STATUS=(
        (1, 'True'),
        (0, 'False'),
    )
    parent=models.ForeignKey('self',blank= True, null=True,related_name='children',on_delete=models.CASCADE)
    slug=models.SlugField()
    title = models.CharField(max_length=150)
    keywords = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to='images/') #hangi klasöre upload edileceğini belirttik.
    status=models.IntegerField(choices=STATUS)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('slug', 'parent',)
        verbose_name_plural = "categories"
    def __str__(self):
        full_path=[self.title]
        k=self.parent
        while k is not None:
            full_path.append(k.title)
            k=k.parent
        return '->'.join(full_path[::-1])

class Product(models.Model):
    STATUS = (
        (1, 'True'),
        (0, 'False'),
    )
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    keywords = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to='images/')
    price=models.FloatField()
    amount=models.IntegerField()
    status=models.IntegerField(choices=STATUS)
    detail=RichTextUploadingField(blank=True)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return  self.title

    def get_cat_list(self):

        k = self.category
        breadcrumb=["dummy"]
        while k is not None:
            breadcrumb.append(k.title)
            k = k.parent
            for i in range(len(breadcrumb) - 1):
                breadcrumb[i] = '/'.join(breadcrumb[-1:i - 1:-1])
        return breadcrumb[-1:0:-1]


class ProductImage(models.Model):

    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    image = models.ImageField(blank=True,upload_to='images/')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)




