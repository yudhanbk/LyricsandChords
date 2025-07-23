from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        
def save(self, commit= True):
        user = super().save(commit= False)
        if commit:
            user.save()
        return user
    
class PostForm(forms.ModelForm):
    caption = forms.CharField(
        max_length=200, 
        widget=forms.Textarea(attrs={'rows':3, 'placeholder': 'Write some caption here'}),
        help_text='Max is 200 characters'
    )
    class Meta:
        model = Post
        fields = ['photo', 'caption']
        widgets = {
            'photo' : forms.FileInput(attrs={'accept': 'image/*'}),
        }
    
    def clean_photo(self):
        photo = self.cleaned_data.get('photo')
        if photo:
            if not photo.content_type.startswith('image/'):
                raise forms.ValidationError('Please upload a valid image')
            
            if photo.size > 5 *1024 * 1024:
                raise forms.ValidationError("Image size is greater than 5 MB")
            return photo
            