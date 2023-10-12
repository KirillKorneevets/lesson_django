from django.db import models



class Posts(models.Model):
    id = models.AutoField(primary_key=True)
    post =  models.CharField(max_length=100)
    text = models.TextField()

    class Meta:
        db_table = 'posts'


class User(models.Model):
    username =  models.CharField(max_length=100)
    age = models.IntegerField()

    class Meta:
        db_table = 'users'



class PostsComments(models.Model):
    text = models.TextField()
    post = models.ForeignKey(Posts, on_delete=models.CASCADE, related_name='comments', default=None)

    class Meta:
        db_table = 'comments'

