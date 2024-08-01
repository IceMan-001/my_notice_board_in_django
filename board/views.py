from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .forms import PostForm
from .models import Post


# Create your views here.
def root(request):
    return render(request, template_name='board/index.html')


def index(request):
    return render(request, template_name='board/index.html')


def about(request):
    context = {
        'name': 'Ivan',
        'lastname': 'Ivanov',
        'email': 'ivanivanov@yandex.ru',

    }
    return render(request, template_name='board/about.html', context=context)


def contacts(request):
    context = {
        'name': 'Тестовый сайт на Django',
        'email': 'd.test@yandex.ru',
        'title': 'Здесь будут контакты'
        }
    return render(request, template_name='board/contacts.html', context=context)


def add_post(request):
    if request.method == 'GET':
        form = PostForm()
        context = {
            'form': form,
            'title': 'Добавление объявления'
        }
        return render(request, template_name='board/add_post.html', context=context)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            # post = Post()
            # post.author = form.cleaned_data['author']
            # post.title = form.cleaned_data['title']
            # post.text = form.cleaned_data['text']
            # post.image = form.cleaned_data['image']
            # post.save()
            form.save(commit=True)

        return index(request)


def post_list_in_table(request):  # Посты в виде таблицы
    # Получаем все объекты модели Post
    posts = Post.objects.all()
    context = {
        'title': 'Посты',
        'posts': posts
    }
    return render(request, template_name='board/posts_in_table.html', context=context)


def post_list(request):
    # Получаем все объекты модели Post
    posts = Post.objects.all()
    context = {
        'title': 'Объявления',
        'posts': posts
    }
    return render(request, template_name='board/posts.html', context=context)


def post_detail(request, pk):
    # получаем объект с заданным первичным ключом
    posts = get_object_or_404(Post, pk=pk)
    # post = Post.objects.get(pk=pk)
    context = {
        'title': 'Информация о посте',
        'posts': posts
    }

    return render(request, template_name='board/post_detail.html', context=context)


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)  # получить объект по ключу
    if request.method == 'POST':
        form = PostForm(data=request.POST, instance=post)
        if form.is_valid():
            form.save()
            return post_list(request)

    else:
        form = PostForm(instance=post)
    context = {
        'form': form,
        'title': 'Редактировать пост'
    }
    return render(request, template_name='board/post_edit.html', context=context)


def post_delete(request, pk):
    # post = get_object_or_404(Post, pk=pk)
    pass
