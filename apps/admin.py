from django.contrib import admin
from apps.forms import UserForm, SkillsForm, ServiceForm, StatisticForm, PortfolioForm, BlogForm, PrizeForm, BlogSinglesForm, OpinionForm
from apps.models import User, Skills, Service, Statistic, Portfolio, Blog, Prize, BlogSingles, Opinion
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    form = UserForm
    
class SkillsAdmin(admin.ModelAdmin):
    forms = SkillsForm

class ServiceAdmin(admin.ModelAdmin):
    forms  = ServiceForm
    
    
class StatisticAdmin(admin.ModelAdmin):
    forms  = StatisticForm
    
    
    
class PortfolioAdmin(admin.ModelAdmin):
    forms  = PortfolioForm
    
    
    
    
class BlogAdmin(admin.ModelAdmin):   
    forms = BlogForm
    
    
class PrizeAdmin(admin.ModelAdmin):   
    forms = PrizeForm 
    
    
    
    
class BlogSinglesAdmin(admin.ModelAdmin):   
    forms = BlogSinglesForm 
    
    
    
    
class OpinionAdmin(admin.ModelAdmin):
    forms = OpinionForm  
    
    
    
admin.site.register(User, UserAdmin)
admin.site.register(Skills, SkillsAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Statistic, StatisticAdmin)
admin.site.register(Portfolio, PortfolioAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Prize, PrizeAdmin)
admin.site.register(BlogSingles, BlogSinglesAdmin)
admin.site.register(Opinion, OpinionAdmin)