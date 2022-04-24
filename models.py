from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.contenttypes.models import ContentType



# Create your models here.
class User(AbstractUser):
    profile_pic=models.ImageField(default='profile_image/de.jpg', upload_to='profile_image')
    bio = models.TextField(null=True,blank=True,max_length=500,default="")

    def get_num_posts(self):
        return post.objects.filter(user=self).count()
    def is_follwoing (self,user_B):
        follwin_condtion = Freinds_con.objects.filter(user_A=self,user_B=user_B).count()
        if follwin_condtion > 0 :
            return True
        else:
            return False
    def get_following(self):
        following= Freinds_con.objects.filter(user_A=self)
        temp = []
        for item in following:
            temp.append(item.user_B.id)
        return temp




class post (models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    caption = models.TextField(max_length=500,null=False)
    date_created = models.DateTimeField(auto_now_add=True , null=False)
    def __str__(self):
        return self.caption
class Freinds_con(models.Model):
    user_A = models.ForeignKey(User,on_delete=models.CASCADE , related_name='user_A')
    user_B = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_B')
    def __str__(self):
        return self.user_A.username + ' & '+ self.user_B.username


