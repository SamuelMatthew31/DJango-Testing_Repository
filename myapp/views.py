from django.shortcuts import render, HttpResponse
from .models import TodoItem


# Create your views here.
def home(request):
    return render(request, "home.html")

def todos(request):
    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        if title:
            TodoItem.objects.create(title=title)

    items = TodoItem.objects.all()

    if request.htmx:
        # request dari HTMX (form submit) → cukup kirim fragment tabel-nya
        return render(request, "partials/_todo_table.html", {"todos": items})

    # request normal / first load → halaman penuh
    return render(request, "todos.html", {"todos": items})


def todo_toggle(request, pk):
    """View baru: toggle status completed satu todo, khusus dipanggil via HTMX."""
    todo = get_object_or_404(TodoItem, pk=pk)
    todo.completed = not todo.completed
    todo.save()

    items = TodoItem.objects.all()
    return render(request, "partials/_todo_table.html", {"todos": items})

def about(request):
    return render(request, "about.html")
