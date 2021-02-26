from django.forms import ModelForm
from .models import *
class GstForm(ModelForm):
    class Meta:
        model = Gst
        fields = "__all__"
