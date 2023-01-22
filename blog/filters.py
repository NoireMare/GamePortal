from django_filters import FilterSet, DateTimeFromToRangeFilter, AllValuesFilter, ModelChoiceFilter, CharFilter
from django_filters.widgets import DateRangeWidget
from .models import Post, Category


class CommentsFilter(FilterSet):
    date = DateTimeFromToRangeFilter(widget=DateRangeWidget(attrs={'type': 'date'}), label='Post date')
    title = AllValuesFilter(label='Post title')
    category_id__name = ModelChoiceFilter(queryset=Category.objects.all())

    class Meta:
        model = Post
        fields = ['date', 'title', 'category_id__name']







