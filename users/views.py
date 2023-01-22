from django.views.generic import CreateView, UpdateView, TemplateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserRegistrationForm, SignInForm, UserProfileForm
from django.urls import reverse_lazy, reverse
from django.shortcuts import render
from .models import User, EmailVerification
from blog.models import Post, Comment
from django.contrib.auth.views import LoginView, LogoutView
from django.http.response import HttpResponseRedirect
from blog.filters import CommentsFilter
import uuid


class UserRegistrationView(CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'users/registration.html'
    success_url = reverse_lazy('log_in')

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        email = EmailVerification.objects.create(code=uuid.uuid4(), user=user)
        email.send_verification_email()
        user.save()
        return super().form_valid(form)


class EmailVerificationView(TemplateView):
    template_name = 'users/email-verification.html'

    def get(self, request, *args, **kwargs):
        code = self.kwargs['code']
        user = User.objects.get(email=self.kwargs['email'])
        email_confirmation = EmailVerification.objects.filter(code=code, user=user)
        if email_confirmation.exists():
            user.is_verified_email = True
            user.is_active = True
            user.is_staff = True
            user.save()
            return super(EmailVerificationView, self).get(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(reverse('/'))


class UserProfileView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = 'users/user-profile.html'

    def get_success_url(self):
        return reverse_lazy('user_profile', args=[self.object.id])


class SignInView(LoginView):
    model = User
    form_class = SignInForm
    template_name = 'users/login.html'

    def get_success_url(self):
        return reverse_lazy('user_profile', args=[self.request.user.id])


class UserLogOutView(LoginRequiredMixin, LogoutView):
    model = User


class PostsByUserView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'users/user-posts.html'

    def get_context_data(self, **kwargs):
        context = super(PostsByUserView, self).get_context_data()
        context['posts'] = Post.objects.filter(author=self.kwargs['pk']).order_by('-date')
        return context


def comments_for_user_posts(request, *args, **kwargs):
    comments = Comment.objects.filter(post__author=request.user.id).order_by('-date')
    posts = Post.objects.filter(id__in=[*comments.values_list('post', flat=True)]).order_by('-date')
    com_filter = CommentsFilter(request.GET, queryset=posts, request=request)
    context = {
        'comments': comments,
        'posts': com_filter.qs,
        'filter': com_filter
    }
    return render(request, 'users/user-comments.html', context)


def approve_comment(request, pk):
    comment = Comment.objects.get(id=pk)
    comment.is_approved = True
    comment.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def delete_comment(request, pk):
    Comment.objects.get(id=pk).delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class UserActivityView(LoginRequiredMixin, TemplateView):
    model = User
    template_name = 'users/user-activity.html'


