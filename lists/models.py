from django.db import models
from django.contrib.auth import get_user_model
from django.forms import ModelForm, HiddenInput

# Create your models here.
class AddEntryForm:
    pass
class List(models.Model):
    name = models.CharField(max_length=50)
    repeats = models.BooleanField()
    user = models.ForeignKey(get_user_model(), models.CASCADE)

    def __str__(self):
        return self.name

    def make_form(self):
        form = AddEntryForm({'lst': self})
        form.fields['lst'].widget = HiddenInput()
        return form
class Entry(models.Model):
    text = models.CharField(max_length=255)
    lst = models.ForeignKey(List, models.CASCADE, db_column="list", related_name="entries")
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.text[:50]

class AddEntryForm(ModelForm):
    class Meta:
        model = Entry
        fields = ('text', 'lst')
        labels = {
            'text': ''
        }
    