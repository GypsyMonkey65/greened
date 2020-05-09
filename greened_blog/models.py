from django.db import models
# django-ckeditor
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
# Top bar

# side catlog first level
class Catlog(models.Model):
    # 这里的意思应该就是 Top 的对象删掉, 这里也会删掉
    text = models.CharField(max_length=50)
    date_added = models.DateTimeField(auto_now_add=True)

    # class Meta:
    #     verbose_name_plural = 'catlog'

    def __str__(self):
        # 返回模型的字符串表示
        return self.text

# Entry
class Article(models.Model):
    # ForeignKey, 外键是一个实例,引用数据库的另一条记录
    # NOT NULL constraint failed: greened_blog_article.topic_id
    # 居然是这里错了, 这里写了个 topic
    catlog = models.ForeignKey(Catlog,on_delete=models.CASCADE)  
    # 增加了 Field 之后, 要在form里修改显示形式才能在html里面显示
    header = models.CharField(max_length=50, blank = True)
    body = RichTextField()
    # body = RichTextUploadingField() 为了上传文件
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'article'

    def __str__(self):
        # 返回模型的字符串表示
        return self.body[:50] + '...'
