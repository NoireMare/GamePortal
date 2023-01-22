from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.timezone import timedelta, now
from django.views.generic import TemplateView, ListView, DetailView, UpdateView
from .models import Post, Category, Comment
from .forms import CreatePostForm, EditPostForm, AddCommentForm
from django.http import HttpResponseRedirect

# Create your views here.


class IndexView(TemplateView):
    template_name = 'blog/index.html'


class PostsListView(ListView):
    model = Post
    template_name = 'blog/blog.html'
    ordering = '-date'
    paginate_by = 5

    def get_queryset(self):
        queryset = super(PostsListView, self).get_queryset()
        category = self.kwargs.get('category')
        return queryset.filter(category=category) if category else queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostsListView, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['today_posts'] = Post.objects.filter(date__gte=now()-timedelta(hours=24))
        return context


class SinglePostView(DetailView):
    model = Post
    template_name = 'blog/blog-post.html'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(SinglePostView, self).get_context_data()
        form = AddCommentForm()
        context['categories'] = Category.objects.all()
        context['comments'] = Comment.objects.filter(post=self.kwargs['pk'], is_approved=True)
        context['form'] = form
        return context

    def post(self, request, *args, **kwargs):
        form = AddCommentForm(data=request.POST)
        if form.is_valid() and request.user.is_authenticated:
            post = Post.objects.get(pk=self.kwargs['pk'])
            Comment.objects.create(text=form.cleaned_data['text'], user=request.user, post=post)
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class EditPostView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = EditPostForm
    template_name = 'blog/edit-post.html'

    def get_success_url(self):
        return reverse_lazy('post_details', args=[self.kwargs['pk']])


def create_post(request):
    if request.method == "POST":
        form = CreatePostForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            title, text, image, category = [form.cleaned_data['title'], form.cleaned_data['text'],
                                            form.cleaned_data['image'], form.cleaned_data['category']]
            author = request.user
            post = Post(title=title, text=text, image=image, category=category, author=author)
            post.save()
            return HttpResponseRedirect(reverse('posts_list'))
    else:
        form = CreatePostForm()
        context = {'form': form}
        return render(request, 'blog/create-post.html', context)


def delete_post(request, pk):
    if request.method == 'POST':
        Post.objects.get(pk=pk).delete()
        return HttpResponseRedirect(reverse_lazy('user_posts', args=[request.user.id]))













