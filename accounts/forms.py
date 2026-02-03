# accounts/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        # Added first_name and last_name so they save to the DB
        fields = ('username', 'email', 'first_name', 'last_name')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # 1. Define the common style for all inputs
        # This matches your Tailwind classes: "w-full bg-[#1f1f1f] ..."
        css_style = "w-full bg-[#1f1f1f] border border-gray-700 rounded-lg px-4 py-3 text-white focus:outline-none focus:border-yellow-500 transition-all"

        # 2. Apply the style to every field automatically
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': css_style})

        # 3. Add specific placeholders (optional but recommended)
        self.fields['email'].widget.attrs.update({'placeholder': 'name@example.com'})
        self.fields['first_name'].widget.attrs.update({'placeholder': 'First Name'})
        self.fields['last_name'].widget.attrs.update({'placeholder': 'Last Name'})


# accounts/forms.py
from django import forms
from django.contrib.auth.forms import AuthenticationForm

class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Match the "Sign Up" input style exactly
        css_style = "w-full bg-[#1f1f1f] border border-gray-700 rounded-lg px-4 py-3 text-white focus:outline-none focus:border-yellow-500 transition-all"
        
        # Apply to username and password fields
        self.fields['username'].widget.attrs.update({
            'class': css_style,
            'placeholder': 'Username'
        })
        self.fields['password'].widget.attrs.update({
            'class': css_style,
            'placeholder': 'Password'
        })