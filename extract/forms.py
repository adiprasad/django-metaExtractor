from django import forms

from .models import MetaInfo

class MetaForm(forms.ModelForm):
	class Meta:
		model = MetaInfo
		fields = ['title','description','keywords']

class URLForm(forms.Form):
	url_name = forms.URLField(required = True,label = '')

