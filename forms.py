from django.core import validators
from django import forms



class RecentProduct(forms.Form):
    mobile = forms.CharField(label='Enter your mobile name')
    re_mobile = forms.CharField(label='Enter your confarm mobile name')
    laptop = forms.CharField(label='Enter your laptop name:',)
    email = forms.EmailField(initial="mukulhossen55@gmail.com", label_suffix= ' = ', validators=[validators.MaxLengthValidator(25)])
    password = forms.CharField(widget=forms.PasswordInput, min_length=8, max_length=16, error_messages={'required': 'Enter Your Password'})
    about = forms.CharField(help_text="Describe about laptop")
    textarea = forms.CharField(widget=forms.Textarea)
    checkbox = forms.CharField(widget=forms.CheckboxInput)
    ram = forms.IntegerField()
    ssd = forms.DecimalField(min_value=1, max_value=5, max_digits=3, decimal_places=2)
    youtube_chanel = forms.BooleanField(label='Subscribe the youtube channel')



    def clean(self):
        cleaned_data = super().clean()
        mobile_match = self.cleaned_data['mobile']
        re_mobile_match = self.cleaned_data['re_mobile']
        if mobile_match != re_mobile_match:
            raise forms.ValidationError("Mobile name dosen't match")
            
           
        
    
    
