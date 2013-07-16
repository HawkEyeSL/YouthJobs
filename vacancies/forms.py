from django import forms
from models import Vacancy
from skills.models import Skill
from django.forms.widgets import CheckboxSelectMultiple
from youthjob.models import Districts
from skills.models import Skill
from django.forms.widgets import CheckboxSelectMultiple

class JobPostingForm(forms.Form):
	title = forms.CharField()
	description = forms.CharField(widget=forms.Textarea)
	district = forms.ModelChoiceField(queryset=Districts.objects.all())

	EXPERIENCE_TYPES = (
		(1, 'Less than 1 year'),
		(2, '1 - 2 years'),
		(3, '2 - 5 years'),
		(4, 'More than 5 years'),
	)

	experience = forms.ChoiceField(choices=EXPERIENCE_TYPES)

	PERSONALITY_TYPES = (
		(1, 'Teamwork'),
		(2, 'Leadership'),
		(3, 'Communication Skills'),
		(4, 'Hard Working'),
	)
	personality = forms.MultipleChoiceField(choices=PERSONALITY_TYPES, widget=CheckboxSelectMultiple()) 

	VACANCY_TYPES = (
		(1, 'IT'),
		(2, 'BPO'),
	)

	vacancy_type = forms.ChoiceField(choices=VACANCY_TYPES)

	SALARY_RANGES = (
        (1, '0 - 20,000'),
        (2, '21,000 - 30,000'),
        (3, '31,000 - 50,000'),
        (4, '51,000 - 75,000'),
        (5, '76,000 - 100,000'),
        (6, '101,000 - 150,000'),
        (7, '151,000 - 200,000'),
        (8, 'above 200,000'),
    )

	salary_ranges = forms.ChoiceField(choices=SALARY_RANGES)

	skills = forms.ModelMultipleChoiceField(queryset=Skill.objects.all(), widget=CheckboxSelectMultiple()) 


