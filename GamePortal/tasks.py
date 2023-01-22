from celery import shared_task
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from .settings import DEFAULT_FROM_EMAIL

from blog.models import Post
from users.models import User
from django.utils.timezone import datetime, timedelta


@shared_task
def send_weekly_news():
    posts = Post.objects.all().exclude(date__lte=datetime.now()-timedelta(days=7))
    users = User.objects.all()
    for user in users:
        html_content = render_to_string(
            'users/email/weekly_news_letter.html',
            {'user': user.username, 'posts': posts})
        msg = EmailMultiAlternatives(
            subject='MMORPG: new posts for the last week up here!',
            body='',
            from_email=DEFAULT_FROM_EMAIL,
            to=[user.email],
        )
        msg.attach_alternative(html_content, "text/html")
        msg.send()

