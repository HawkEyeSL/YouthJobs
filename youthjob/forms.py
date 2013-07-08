from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegistrationForm(UserCreationForm):
	CHOICES = ((0, 'Applicant'), (1, 'Company'),)
	email = forms.EmailField(required=True)
	full_name = forms.CharField(required=True)
	type = forms.TypedChoiceField(
		coerce=lambda x: x == 'True', 
		choices=((False, 'Applicant'), (True, 'Company')), 
		widget=forms.RadioSelect
	)
	
	class Meta:
		model = User
		fields = ('type', 'username', 'full_name', 'email','password1', 'password2',)

	def save(self, commit=True):
		user = super(UserCreationForm, self).save(commit=False)
		user.set_password(self.cleaned_data["password1"])
		user.email = self.cleaned_data['email']
		user.first_name = self.cleaned_data['full_name']
		user.is_staff = self.cleaned_data['type']
		
		if commit:
			user.save()

		return user