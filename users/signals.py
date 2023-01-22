from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.loader import render_to_string
from GamePortal.settings import DEFAULT_FROM_EMAIL

from blog.models import Comment
from django.core.signals import request_finished


@receiver(post_save, sender=Comment)
def send_email_after_receiving_comment(sender, instance, created, **kwargs):
    if not instance.is_approved:
        if created:
            subject = f'MMORPG Portal: {instance.user} has added comment to your post'
        else:
            subject = f'MMORPG Portal: {instance.date.strftime("%d.%m.%Y")} {instance.user} has changed his comment'
        html_content = render_to_string(
            'users/email/email_confirmation_of_comment.html',
            {'form': [instance.user, instance.date, instance.text, instance.post]})
        msg = EmailMultiAlternatives(
            subject=subject,
            body=instance.text,
            from_email=DEFAULT_FROM_EMAIL,
            to=[instance.post.author.email],
        )
    else:
        subject = f'MMORPG Portal: {instance.post.author} has approved your comment'
        html_content = render_to_string(
            'users/email/email_approval_of_comment.html',
            {'form': [instance.user, instance.date, instance.text, instance.post]})
        msg = EmailMultiAlternatives(
            subject=subject,
            body=instance.text,
            from_email=DEFAULT_FROM_EMAIL,
            to=[instance.user.email],
            )
    msg.attach_alternative(html_content, "text/html")
    msg.send()


