from django import forms
from models import Vacancy
from skills.models import Skill
from django.forms.widgets import CheckboxSelectMultiple

class JobPostingForm(forms.ModelForm):

	#district = forms.ModelChoiceField(Districts.objects.all().values_list('name', flat=True))

	class  Meta:
		model = Vacancy
		fields = ('name', 'description', 'district', 'experience', 'personality','vacancy_type', 'salary_ranges')
