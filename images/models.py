from django.db import models

# Create your models here.

class Category(models.Model):
    visible_name = models.CharField(max_length=128, blank=True, null=True)
    friendly_link = models.CharField(max_length=128)
    display = models.BooleanField(default=True)
    display_as_category = models.BooleanField(default=True)
    relase_date = models.DateTimeField(auto_now=True)
    background_image = models.ImageField(upload_to="pics/main_images/categories", blank=True, null=True)

    def __str__(self):
        return self.visible_name

class Group(models.Model):
    visible_name = models.CharField(max_length=128, blank=True, null=True)
    friendly_link = models.CharField(max_length=128)
    display = models.BooleanField(default=True)
    relase_date = models.DateTimeField(auto_now=True)
    background_image = models.ImageField(upload_to="pics/main_images/groups", blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.visible_name + " z kategorii " +str(self.category)

class Image(models.Model):
    visible_name = models.CharField(max_length=128, blank=True, null=True)
    friendly_link = models.CharField(max_length=128)
    display = models.BooleanField(default=True)
    relase_date = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to="pics")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    def get_groups(self):
        groups = Group.objects.filter(category=self.category)
        return groups
    def __str__(self):
        return self.visible_name + " z grupy " +str(self.group)