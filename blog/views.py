from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import BlgPost, BlgCategory
from .forms import BlgPostForm, BlgEditForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator

# Create your views here.


class BlgHomeView(ListView):
    model = BlgPost  # from the class Post in models.py
    template_name = 'blog/blg_index.html'
    ordering = ['-post_date']
    context_object_name = 'posts'
    paginate_by = 7
    queryset = BlgPost.objects.all()

    def get_context_data(self, *args, **kwargs):
        cat_menu = BlgCategory.objects.all()
        context = super(BlgHomeView, self).get_context_data(*args, **kwargs)
        context['cat_menu'] = cat_menu

        return context

    # def post_list(request):
    #     object_list = Post.published.all()
    #     paginator = Paginator(object_list, 3) # 3 posts in each page
    #     page = request.GET.get('page')
    #     try:
    #         posts = paginator.page(page)
    #     except PageNotAnInteger:
    #         # If page is not an integer deliver the first page
    #         posts = paginator.page(1)
    #     except EmptyPage:
    #         # If page is out of range deliver last page of results
    #         posts = paginator.page(paginator.num_pages)
    #     return render(request,
    #                   'blog/post/list.html',
    #                    {'page': page,
    #                     'posts': posts})



def BlgCategoryView(request, cats):
    category_posts = BlgPost.objects.filter(category=cats)
    cat_menu = BlgCategory.objects.all()
    cats = cat_menu[int(cats)-1]
    return render(request, 'blog/blg_cat.html', {'cats': cats, 'category_posts':category_posts, 'cat_menu': cat_menu})


class BlgDetailView(DetailView):
    model = BlgPost
    template_name = 'blog/blg_detail.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = BlgCategory.objects.all()
        context = super().get_context_data(**kwargs)
        # total_likes = stuff.total_likes()
        context['cat_menu'] = cat_menu
        context['post'] = get_object_or_404(BlgPost, id=self.kwargs['pk'])
        # context["total_likes"] = total_likes
        return context


class AddBlgPostView(CreateView):
    model = BlgPost
    form_class = BlgPostForm
    template_name = 'blog/blg_add.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = BlgCategory.objects.all()
        context = super(AddBlgPostView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

    # fields = '__all__'  # means all fields are ok, if not specify the fields
    # fields = ('title', 'body')  ----> if want to show only title and body in add_post page '''


# class AddCategoryView(CreateView):
#     model = Category
#     template_name = 'add_category.html'
#     fields = '__all__'  # means all fields are ok, if not specify the fields


class EditBlgPostView(UpdateView):
    model = BlgPost
    form_class = BlgEditForm
    template_name = 'blog/blg_edit.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = BlgCategory.objects.all()
        context = super(EditBlgPostView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context


    # fields = ['title', 'title_tag', 'body']  # no need to edit author


class DeleteBlgPostView(DeleteView):
    model = BlgPost
    template_name = 'blog/blg_delete.html'
    success_url = reverse_lazy('blg_index')
