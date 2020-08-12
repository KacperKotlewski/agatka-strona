import django.forms as forms
from .models import Category, Group, Image
from datetime import datetime 

class GroupForm(forms.ModelForm):
    visible_name = forms.CharField(
        widget=forms.TextInput(attrs={
                'placeholder': 'Nazwa grupy zdjęć',
                'class' : "form-control",
                'autocomplete':'off'
            }),
        label = "Nazwa"
    )
    friendly_link = forms.CharField(
        widget=forms.TextInput(attrs={
                'placeholder': 'Przyjazny link',
                'class' : "form-control",
                'autocomplete':'off'
            }),
        label = "Link"
    )
    display = forms.BooleanField(
        widget=forms.CheckboxInput(),
        label = "Grupa widoczna",
        initial=True,
        required=False
    )
    relase_date = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={
                'class' : "form-control",
                'autocomplete':'off'
            }),
        initial = datetime.now,
        label = "Data wyświetlenia"
    )
    background_image = forms.FileField(
        widget=forms.FileInput(attrs={
                'class' : "form-control",
                'autocomplete':'off',
                "accept":"image/*"
            }),
        label = "Wybierz zdjęcia"
    )
    cat = forms.DecimalField(
        widget=forms.HiddenInput(),
        label = False
    )
    category = forms.Field(
        widget=forms.HiddenInput(),
        required = False,
        label = False
    )

    class Meta:
        model = Group
        fields = ('visible_name', 'friendly_link', 'display', 'relase_date', 'background_image', 'category')
    
    def clean_friendly_link(self, *args, **kwargs):
        friendly_link = self.cleaned_data["friendly_link"]
        friendly_link = friendly_link.replace(" ", "-")
        category = Category.objects.filter(id=self.data.get("cat"))

        try:
            groups = Group.objects.filter(category=category, friendly_link=friendly_link)
            if groups.count != 0:
                print("Taki link już istnieje w tej kategorii") 
                raise forms.ValidationError("Taki link już istnieje w tej kategorii") 

        except:
            pass
        return friendly_link

    def clean_category(self, *args, **kwargs):
        category = Category.objects.filter(id=int(self.data.get("cat")))
        return category[0]



class ImageForm(forms.ModelForm):
    image = forms.FileField(
        widget=forms.FileInput(attrs={
                'class' : "form-control",
                'autocomplete':'off',
                "accept":"image/*"
            }),
        label = "Wybierz zdjęcia"
    )

    cat = forms.DecimalField(
        widget=forms.HiddenInput(),
        label = False
    )
    grp = forms.DecimalField(
        widget=forms.HiddenInput(),
        label = False
    )
    category = forms.Field(
        widget=forms.HiddenInput(),
        required = False,
        label = False
    )
    group = forms.Field(
        widget=forms.HiddenInput(),
        required = False,
        label = False
    )
    friendly_link = forms.CharField(
        widget=forms.HiddenInput(),
        required = False,
    )

    visible_name = forms.CharField(
        widget=forms.HiddenInput(),
        required = False,
    )
    display = forms.BooleanField(
        widget=forms.HiddenInput(),
        initial=True,
    )
    relase_date = forms.DateTimeField(
        widget=forms.HiddenInput(),
        initial = datetime.now,
    )

    class Meta:
        model = Image
        fields = ('image', 'friendly_link', 'visible_name', 'display', 'relase_date', "category", "group")


    def clean_category(self, *args, **kwargs):
        category = Category.objects.filter(id=int(self.data["cat"]))
        return category[0]

    def clean_group(self, *args, **kwargs):
        group = Group.objects.filter(id=int(self.data["grp"]))
        return group[0]
    
    def clean_friendly_link(self, *args, **kwargs):
        friendly_link = self.data.get("friendly_link")
        if friendly_link == "":
            friendly_link = str(self.cleaned_data.get("image").name.split(".")[0])
        friendly_link = friendly_link.replace(" ", "_")
        group = Group.objects.filter(id=self.data.get("grp"))[0]
        
        last_i = ""
        for i in range(99999):
            print("friendly_link:'",friendly_link+last_i,"'")
            image = Image.objects.filter(group=group, friendly_link=(friendly_link+last_i))
            if image.count() == 0:
                return friendly_link
            last_i = str(i)

    def clean_visible_name(self, *args, **kwargs):
        visible_name = self.cleaned_data.get("friendly_link")
        return visible_name


class ImageForm2(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('visible_name', 'friendly_link', 'display', 'relase_date', 'image', 'category', 'group')
        widgets = {
            'image': forms.ClearableFileInput(attrs={'multiple': True}),
        }