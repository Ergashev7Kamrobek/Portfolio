from django.db.models import Model, CharField, EmailField, ForeignKey, CASCADE,PositiveIntegerField,ImageField,TextField,URLField, DateTimeField

# Create your models here.


class User(Model):
      first_name = CharField(verbose_name='ism', max_length=222, null=True, blank=True)
      last_name = CharField(verbose_name='familya', max_length=200)
      username = CharField(max_length=200, unique=True)
      job = CharField(verbose_name='kasbi', max_length=200)
      phone_number = CharField(verbose_name='telofon raqami', max_length=30)
      email = EmailField(verbose_name='pochta manzil', max_length=150, unique=True)
      image = ImageField(null=True, blank=True)
      about_me = TextField(null=True, blank=True)
      
      
      def get_full_name(self):
         return self.first_name + ' ' + self.last_name
      
      
      
      
      
class Skills(Model):
    user = ForeignKey("apps.User", on_delete=CASCADE)
    title = CharField(verbose_name='skill nomi', max_length=150)
    level = PositiveIntegerField()
    
    
    
    
          
class Statistic(Model):
    number = PositiveIntegerField(default=0)
    title = CharField(max_length=150)
   
    
    
    
    
    
    
class Service(Model):
    title = CharField(max_length=150, null=True, blank=True)
    short_comment = TextField(null=True, blank=True )

    
    
    
    
    
class Portfolio(Model):
  image_main = ImageField(null=True, blank=True, upload_to= "Portfolio")
  image_details = ImageField(null=True, blank=True, upload_to= "Portfolio_details")
  name = CharField(max_length=100, null=True, blank=True)
  category = CharField(max_length=111, null=True, blank=True )
  upload_date = CharField(max_length=111, null=True, blank=True) 
  client = CharField(max_length=100, null=True, blank=True)
  project_date = CharField(max_length=202, null=True, blank=True)
  project_url = URLField()
  about_project = TextField(null=True, blank=True)
    
    
    
    



class Blog(Model):
    img = ImageField(null=True, blank=True, upload_to="Blog")
    category = CharField(max_length=111, null=True, blank=True )
    title = CharField(max_length=150, null=True, blank=True)
    text = TextField(max_length=150, null=True, blank=True)
    upload_at = DateTimeField(auto_now_add=True)
    
    
    
class Prize(Model):
    number = PositiveIntegerField(default=0)
    title = CharField(max_length=150, null=True, blank=True)
    
    
    
    
class BlogSingles(Model):
    title = CharField(max_length=150, null=True, blank=True)
    text = TextField(max_length=150, null=True, blank=True)
    recent_post = CharField(max_length=150, null=True, blank=True)
    archives =  CharField(max_length=150, null=True, blank=True)
    tags = CharField(max_length=150, null=True, blank=True)
    coment = PositiveIntegerField()
    
    
    
    
    
    
    
    
class Comment(Model):
    fullname = CharField(max_length=120, blank=True, null=True)
    email = EmailField(max_length=120, blank=True, null=True)
    post_id = ForeignKey("apps.Blog", on_delete=CASCADE)
    text = TextField()
    created_at = DateTimeField(auto_now=True)
    
    
    
class Opinion(Model):
    user = ForeignKey("apps.User", on_delete=CASCADE)
    text = TextField(null=True, blank=True)
    