from django.db.models.base import Model
from django.forms import ModelForm
from .models import Project

class ProjectForm(ModelForm):
	class Meta:
		model= Project
		fields = ['title', 'description', 'demo_link','source_link', 'tags']