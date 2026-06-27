from django.db import models

# Create your models here.
class User(models.Model):
    class UserRole(models.TextChoices):
        REGISTRAR = 'REGISTRAR','Registrar'
        ATTENDEE = 'ATTENDEE','Attendee'

    event = models.ManyToManyField('event.EventList')
    user_id = models.CharField(max_length=50,unique=True,editable=False,blank=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    profile_image = models.ImageField(upload_to='user/profile',null=True,blank=True)
    role = models.CharField(max_length=50,choices=UserRole.choices,default=UserRole.ATTENDEE)
    is_verified = models.BooleanField(default=False)
    joined_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self,*args,**kwargs):
        new = self.pk is None
        super().save(*args,**kwargs)

        if new and not self.user_id:
            self.user_id = f"USR-{self.pk:03d}"
            User.objects.filter(pk=self.pk).update(user_id=self.user_id)

    def __str__(self):
        return f"{self.id}--{self.first_name} {self.last_name}"

