from django import forms
from apps.models import User, Skills, Service, Statistic, Portfolio, Blog, Prize, BlogSingles, Opinion



# class SignUpForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ('first_name', 'last_name', 'username', 'email', 'job', 'password1', 'password2' )
#         # fields = '__all__'

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'job', 'phone_number', 'image', 'about_me' )
        # fields = '__all__'



class SkillsForm(forms.ModelForm):
    
    class Meta:
        model = Skills
        fields = ('title', 'level')






class ServiceForm(forms.ModelForm):
    
    class Meta:
        model = Service
        fields = ('title', 'short_comment')





class StatisticForm(forms.ModelForm):
    
    class Meta:
        model = Statistic
        fields = ('number', 'title')








class PortfolioForm(forms.ModelForm):
    
    class Meta:
        model = Portfolio
        # fields = ('image', 'name', 'category', 'upload_date' )
        fields = "__all__"






class BlogForm(forms.ModelForm):
    
    class Meta:
        model = Blog
        # fields = ('image', 'name', 'category', 'upload_date' )
        fields = "__all__"






class PrizeForm(forms.ModelForm):
    
    class Meta:
        model = Prize
        fields = ('number', 'title')
        
        
        
        
        
        
class BlogSinglesForm(forms.ModelForm):
    
    class Meta:
        model = BlogSingles
        fields = "__all__"
        
        
        
        
        
        
        
        
class OpinionForm(forms.ModelForm):
    class Meta:
        model = Opinion
        fields = "__all__"