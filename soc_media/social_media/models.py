from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=18, null=False, blank=False)
    lastname = models.CharField(max_length=18, null=False, blank=False)
    email = models.EmailField( null=False, blank=False)
    username = models.CharField(max_length=18, null=False, blank=False, unique=True)
    phone_number = models.CharField(max_length=18, null=False, blank=False)
    password = models.CharField(max_length=180)


class Post(models.Model ):
    customer = models.ForeignKey("Customer", on_delete=models.CASCADE)
    title = models.CharField(max_length=180,null=False, blank=False )
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    customer = models.ForeignKey("Customer", on_delete=models.CASCADE)
    post = models.ForeignKey("Post", on_delete=models.CASCADE)
    commented_at = models.DateTimeField(auto_now_add=True)
    comment = models.TextField()
    
class Like(models.Model):
    customer = models.ForeignKey("Customer", on_delete=models.CASCADE)
    post = models.ForeignKey("Post", on_delete=models.CASCADE)
    liked_at = models.DateTimeField(auto_now_add=True)