from django.db import models


class ContentItem(models.Model):

    CATEGORY_CHOICES = [
        ("analysis", "تحلیل‌ها"),
        ("signals", "سیگنال‌ها"),
        ("students", "رضایت دانشجویان"),
    ]

    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        verbose_name="دسته"
    )

    title = models.CharField(
        max_length=200,
        verbose_name="عنوان"
    )

    text = models.TextField(
        blank=True,
        verbose_name="متن"
    )

    image = models.ImageField(
        upload_to="content/",
        blank=True,
        null=True,
        verbose_name="تصویر"
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="تاریخ ایجاد"
    )

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "محتوا"
        verbose_name_plural = "محتوا"

    def str(self):
        return self.title