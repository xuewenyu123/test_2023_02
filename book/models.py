from django.db import models

# Create your models here.


class BookInfo(models.Model):

    name = models.CharField(max_length=10, unique=True)
    pub_date = models.DateField(null=True)  # 发布日期
    readcount = models.IntegerField(default=0)  # 阅读量
    commentcount = models.IntegerField(default=0)  # 评论量
    is_delete = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "bookinfo"
        verbose_name = "书籍管理"


class PersonInfo(models.Model):
    GENDER_CHOICE = (
        (1, "male"),
        (2, "female"),
    )

    name = models.CharField(max_length=10)
    gender = models.SmallIntegerField(choices=GENDER_CHOICE, default=1)
    description = models.CharField(max_length=30, null=True)
    is_delete = models.BooleanField(default=False)
    book = models.ForeignKey("BookInfo", on_delete=models.CASCADE)

    class Meta:
        db_table = "personinfo"
