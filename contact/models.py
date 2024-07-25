from django.db import models


SUBMITTED, CANCEL, READIED, ANSWERED, AGREED, ACCEPTED = 'Kontakt yuborilgan', 'Rad etish', 'Xabar o\'qildi', 'Javob berilgan', 'Kelishilgan', 'Zakaz olingan'


class Contact(models.Model):
    CONTACT_STATUS = (
        (SUBMITTED, 'Kontakt yuborilgan'),
        (CANCEL, 'Rad etish'),
        (READIED, 'Xabar o\'qildi'),
        (AGREED, 'Kelishilgan'),
        (ACCEPTED, 'Zakaz olingan'),
        (ANSWERED, 'Javob berilgan')
    )

    fullname = models.CharField(max_length=150, verbose_name='To\'liq ism')
    phone = models.CharField(max_length=20, verbose_name='Telefon raqam')
    message = models.TextField(verbose_name='Maqsad')
    created_at = models.DateField(auto_now_add=True, verbose_name='Yozilgan vaqt')
    status = models.CharField(max_length=30, choices=CONTACT_STATUS, default=SUBMITTED, verbose_name='Holati')

    def __str__(self):
        return f"{self.fullname} - {self.phone}"

    objects = models.Manager()

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Kontakt '
        verbose_name_plural = 'Kontaktlar'
        db_table = 'contacts'
