from django.db import models

from posts.utils import upload_image_to_telegraph


class Project(models.Model):
    title = models.CharField(max_length=250, verbose_name='Sarlavha')
    image = models.ImageField(upload_to='projects/images/', null=True, blank=True, verbose_name='Rasm')
    image_url = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True, verbose_name='Tavsifi')
    price = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True, verbose_name='Narxi')
    url = models.CharField(max_length=200, null=True, blank=True, verbose_name='Manzil')
    start_date = models.DateField(null=True, blank=True, verbose_name='Boshlangan kuni')
    end_date = models.DateField(null=True, blank=True, verbose_name='Yakunlangan kuni')
    created_at = models.DateField(auto_now_add=True, verbose_name='Yaratilgan vaqt')

    def __str__(self):
        return self.title

    objects = models.Manager()

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Loyiha '
        verbose_name_plural = 'Loyihalar'
        db_table = 'projects'

    def save(self, *args, **kwargs):
        if not self.pk:
            super().save(*args, **kwargs)
            self.upload_image()
        super().save(*args, **kwargs)

    def upload_image(self):
        self.image_url = upload_image_to_telegraph(self.image)
        self.save()


class ProjectImage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='images', verbose_name='Loyiha')
    image = models.ImageField(upload_to='projects/images', null=True, blank=True, verbose_name='Rasm')
    image_url = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Qoshilgan vaqt')

    def __str__(self):
        return self.project.title

    class Meta:
        verbose_name = 'Loyiha Rasimi '
        verbose_name_plural = 'Loyihalar Rasimi'
        db_table = 'project_images'

    def save(self, *args, **kwargs):
        if not self.pk:
            super().save(*args, **kwargs)
            self.upload_image()
        super().save(*args, **kwargs)

    def upload_image(self):
        self.image_url = upload_image_to_telegraph(self.image)
        self.save()


class Comment(models.Model):
    COMMENT_RANK = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5')
    )

    user = models.CharField(max_length=255, verbose_name='To\'liq ism')
    date = models.DateField(verbose_name='Kun')
    project = models.ForeignKey(to=Project, on_delete=models.CASCADE, verbose_name='Loyiha')
    comment = models.TextField(verbose_name='Komentariya')
    rank = models.CharField(max_length=3, choices=COMMENT_RANK, default='5', verbose_name='Baho')

    def __str__(self):
        return f"{self.user} - {self.project.title}"

    objects = models.Manager()

    class Meta:
        ordering = ['-date']
        verbose_name = 'Komentariya '
        verbose_name_plural = 'Komentariyalar'
        db_table = 'comments'


class Tariff(models.Model):
    title = models.CharField(max_length=250, verbose_name='Sarlavha')
    description = models.TextField(verbose_name='Tavsifi')
    start_amount = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=False,
                                       verbose_name='Boshlang\'ich narx')
    value = models.ForeignKey('Project_Type', on_delete=models.CASCADE, related_name='tariffs',
                              verbose_name='Proektning tarifi')

    # value = models.ForeignKey('Project_Type', on_delete=models.CASCADE, related_name='Proektning tarifi')

    def __str__(self):
        return f"{self.title}"

    objects = models.Model

    class Meta:
        verbose_name = 'Tarif '
        verbose_name_plural = 'Tariflar'
        db_table = 'tariffs'


class Project_Type(models.Model):
    value = models.CharField(max_length=60, verbose_name='Proektning nomi')
    title = models.CharField(max_length=250, verbose_name='Sarlavha')
    description = models.TextField(verbose_name='Tavsifi')

    def __str__(self):
        return f"{self.value}"

    objects = models.Manager()

    class Meta:
        verbose_name = 'Loyiha Turini '
        verbose_name_plural = 'Loyihalar Turlari'
        db_table = 'project_types'


SUBMITTED, REJECTED, ACCEPTED, AGREED, NOT_AGREED, CONTINUE_PROJECT, SUCCESSFULLY = 'Ariza yuborilgan', 'Rad etish', 'Qabul qilingan', 'Kelishilgan', 'Kelishilmagan', 'Davom etayotgan proyekt', 'Tugatilgan proyekt'


class Order(models.Model):
    PROJECT_STATUS = (
        (SUBMITTED, 'Ariza yuborilgan'),
        (REJECTED, 'Rad etish'),
        (ACCEPTED, 'Qabul qilingan'),
        (AGREED, 'Kelishilgan'),
        (NOT_AGREED, 'Kelishilmagan'),
        (CONTINUE_PROJECT, 'Davom etayotgan proyekt'),
        (SUCCESSFULLY, 'Tugatilgan proyekt'),
    )

    fullname = models.CharField(max_length=30, verbose_name='To\'liq ism')
    phone = models.CharField(max_length=30, verbose_name='Telefon raqam')
    project_type = models.ForeignKey(to=Project_Type, on_delete=models.CASCADE, verbose_name='Loyiha turi')
    tariff = models.ForeignKey(to=Tariff, on_delete=models.CASCADE, verbose_name='Tarif')
    message = models.TextField(verbose_name='Maqsad')
    status = models.CharField(max_length=30, choices=PROJECT_STATUS, default=SUBMITTED, verbose_name='Holati')
    create_time = models.DateField(auto_now_add=True, verbose_name='Jonatilgan vaqti')

    def __str__(self):
        return f"{self.fullname} - {self.phone}"

    objects = models.Manager()

    class Meta:
        verbose_name = 'Buyurtma '
        verbose_name_plural = 'Buyurtmalar'
        db_table = 'orders'
