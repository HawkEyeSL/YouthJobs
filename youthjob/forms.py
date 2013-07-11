from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from models import Applicants, Companies, Districts
from django.forms import extras
import datetime

class CompanyDetailsForm(forms.ModelForm):

	#district = forms.ModelChoiceField(Districts.objects.all().values_list('name', flat=True))

	class  Meta:
		model = Companies
		fields = ('name', 'company_reg_no', 'address', 'phone1', 'phone2', 'district', 'type', 'postal_code',)

class ApplicantDetailsForm(forms.ModelForm):
	gender = forms.TypedChoiceField(
		coerce=lambda x: x == 'True', 
		choices=((True, 'Male'), (False, 'Female')), 
		widget=forms.RadioSelect
	)

	this_year = datetime.date.today().year
	birth_date = forms.DateField(widget=extras.SelectDateWidget(years=range(this_year-50, this_year+1)))

	#district = forms.ModelChoiceField(Districts.objects.all().values_list('name', flat=True))

	class  Meta:
		model = Applicants
		fields = ('full_name', 'birth_date', 'gender', 'address','district' ,'phone',)

class UserRegistrationForm(UserCreationForm):
	email = forms.EmailField(required=True)
	type = forms.TypedChoiceField(
		coerce=lambda x: x == 'True', 
		choices=((False, 'Applicant'), (True, 'Company')), 
		widget=forms.RadioSelect
	)
	
	class Meta:
		model = User
		fields = ('type', 'username', 'email','password1', 'password2',)

	def save(self, commit=True):
		user = super(UserCreationForm, self).save(commit=False)
		user.set_password(self.cleaned_data["password1"])
		user.email = self.cleaned_data['email']
		user.is_staff = self.cleaned_data['type']
		
		if commit:
			user.save()

		return user