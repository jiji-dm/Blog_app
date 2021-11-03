from django.contrib import admin
from .models import BlogPost    #modelsクラスからBlogPostをインポート

admin.site.register(BlogPost)
#Django管理サイトにBlogPostを登録する