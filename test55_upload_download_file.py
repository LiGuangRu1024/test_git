# @time     ：2024/7/22 10:59
# @author   : 莉光哈哈哈
# @file     : test55_upload_download_file.py
# @software : PyCharm
'''
1.确保你的Django项目已经创建并且安装了django.contrib.staticfiles应用，这个应用负责处理静态文件，虽然主要是用于CSS、JS等，但在处理文件上传下载时也有间接关联。
'''
import os.path

'''
2. 配置MEDIA_URL和MEDIA_ROOT----在你的settings.py文件中，需要设置MEDIA_URL和MEDIA_ROOT，这两个设置告诉Django如何处理上传的文件
'''
MEDIA_URL = '/media/'  # URL前缀，用于访问上传的文件
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')  # 文件系统中的路径，用于存储上传的文件

'''
确保在你的主URL配置文件中添加了媒体文件的处理路由。如果你使用的是默认的urls.py，可以这样添加：
'''
from diango.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  # 其他路由
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

'''
注意：在生产环境中，你应该配置Web服务器（如Nginx、Apache）来处理媒体文件，而不是使用Django来直接服务这些文件。
'''

'''
3.创建模型和表单----假设在一个博客应用中添加文件上传功能
'''
# 模型（model.py）
from django.db import models


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    # upload_to参数指定了上传文件保存的子目录。
    file_upload = models.FileField(upload_to='uploads/', blank=True, null=True)

    def __str__(self):
        return self.title


# 表单（form.py）
from django import forms
from .models import BlogPost


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'file_upload']


'''
4.视图函数(view.py)
'''
'''
上传视图
'''
from django.shortcuts import render, redirect
from .forms import BlogPostForm


def upload_file(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('file_list')  # 重定向到文件列表页

    else:
        form = BlogPostForm()
    return render(request, 'upload_form.html', {'form': form})


'''
下载视图
'''
from django.http import FileResponse
from .models import BlogPost


def download_file(request, post_id):
    blog_post = get_object_or_404(BlogPost, pk=post_id)
    if blog_post.file_upload:
        filename = os.path.basename(blog_post.file_upload.name)
        response = FileResponse(open(blog_post.file_upload.path, 'rb'), as_attachment=True, filename=filename)
        return response
    else:
        # 如果没有文件，则返回错误页面或重定向
        pass


'''
5.URL配置-----在你的应用的urls.py中添加对应的URL映射
'''
from djingo.urls import path
from . import views

urlpatterns=[
    path('upload/',views.upload_file,name='upload'),
    path('download/<int:post_id>/',views.download_file,name='download'),
]

'''
6.HTML模板-----创建一个简单的HTML模板upload_form.html来渲染上传菜单
'''