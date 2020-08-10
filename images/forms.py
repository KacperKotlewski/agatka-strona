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
        widget=forms.CheckboxInput(attrs={
                'class' : ""
            }),
        label = "Grupa ukryta",
        required=False,
        initial=""
    )
    relase_date = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={
                'class' : "form-control",
                'autocomplete':'off'
            }),
        initial = datetime.now,
        label = "Data wyświetlenia"
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
        print("Taki link nie istnieje w tej kategorii") 
        return friendly_link

    def clean_category(self, *args, **kwargs):
        category = Category.objects.filter(id=int(self.data.get("cat")))
        return category[0]

    def save(self, commit=True, *args, **kwargs):
        instance = super(GroupForm, self).save(commit=False)
        if commit:
            instance.save()
        return instance

class GroupForm2(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['background_image']



class ImageForm(forms.ModelForm):
    visible_name = forms.CharField(
        widget=forms.TextInput(attrs={
                'placeholder': 'Nazwa grupy zdjęć',
                'class' : "form-control"
            }),
        label = "Nazwa"
    )

    class Meta:
        model = Image
        fields = ['visible_name']
