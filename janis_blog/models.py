from django.db import models
from django.utils import timezone

# models.Model 用來定義Django模型，POST為模型的名字
class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    #blank=True，允許輸入空值
    published_date = models.DateTimeField(
            blank=True, null=True)
    picture = models.URLField(blank=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
