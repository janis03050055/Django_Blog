from django.contrib import admin
from .models import Post

#讓我們的模型在admin頁面上可見，用下列方法註冊模型
admin.site.register(Post)
