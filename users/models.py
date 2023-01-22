from django.db import models
from django.urls import reverse
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    image = models.ImageField(upload_to='user_images', blank=True, null=True)


class EmailVerification(models.Model):
    code = models.UUIDField(unique=True)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)

    def send_verification_email(self):
        link = reverse('email_verify', kwargs={'email': self.user.email, 'code': self.code})
        full_link = f'{settings.DOMAIN_NAME}{link}'
        subject = f'{settings.SITE}: Активация учётной записи для {self.user.username}'
        text = 'Для завершения регистрации на сайте {}, перейдите по ссылке {} '.format(
            settings.SITE,
            full_link
        )
        send_mail(
            subject=subject,
            message=text,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[self.user.email],
            fail_silently=False,
        )






