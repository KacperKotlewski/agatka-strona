from django.db import models

# Create your models here.

class Category(models.Model):
    visible_name = models.CharField(max_length=128, blank=True, null=True)
    friendly_link = models.CharField(max_length=128, unique=True)
    display = models.BooleanField(default=True)
    display_as_category = models.BooleanField(default=True)
    relase_date = models.DateTimeField()
    background_image = models.ImageField(upload_to="pics/images", blank=True, null=True)

    def __str__(self):
        return "''"+self.visible_name+"''"

def get_upload_path_for_group(instance, filename):
    return 'pics/images/{0}/{1}'.format(instance.category.friendly_link, filename)
def get_upload_path_for_image(instance, filename):
    return 'pics/images/{0}/{1}/{2}'.format(instance.category.friendly_link, instance.group.friendly_link, filename)

class Group(models.Model):
    visible_name = models.CharField(max_length=128, blank=True, null=True)
    friendly_link = models.CharField(max_length=128)
    display = models.BooleanField(default=True)
    relase_date = models.DateTimeField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    background_image = models.FileField(upload_to=get_upload_path_for_group, blank=True, null=True)

    def __str__(self):
        return "''"+self.visible_name + "'' z kategorii " +str(self.category)

class Image(models.Model):
    visible_name = models.CharField(max_length=128, blank=True, null=True)
    friendly_link = models.CharField(max_length=128)
    display = models.BooleanField(default=True)
    relase_date = models.DateTimeField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=get_upload_path_for_image)

    def get_groups(self):
        groups = Group.objects.filter(category=self.category)
        return groups
    def __str__(self):
        return "''"+self.visible_name + "'' z grupy " +str(self.group)

    def create(self, **kwargs):
        obj = self.model(**kwargs)
        self._for_write = True
        return obj