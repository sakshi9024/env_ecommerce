from django.db import models
from django.contrib.auth.models import User
from base.models import BaseModel
from django.db.models.signals import post_save
from django.dispatch import receiver
import uuid
from base.emails import send_account_activation_email

# we need to override django user model because
# we need to store the details of user for this modern ecommerce project
# django user model doesnot have the capability to check what is the mobile number of user , user is verified or not or what is the email of user ....so that's why we need to create this models
# django models contains specific things it doest not have isverify , token system ...so for that we will use one to one field 
# Create your models here.


class Profile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE , related_name="profile" )
    is_email_verified = models.BooleanField(default=False)
    email_token = models.CharField(max_length=100 , null=True, blank = True)
    profile_image= models.ImageField(upload_to='profile')

@receiver(post_save,sender = User)
def send_email_token(sender, instance , created, **kwargs):
    try:
        if created:
            email_token = str(uuid.uuid4())   # we will generate uuid or we can say email token and we'll convert to string so that no issue come
            email = instance.email   # verfication email will be
            send_account_activation_email(email, email_token)  #now we will create this function so that uuid will automatically populate....
    
    except Exception as e:
        print(e)

