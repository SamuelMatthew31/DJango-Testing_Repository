from django.shortcuts import render, HttpResponse
from .models import TodoItem
from .forms import ContactForm


# Create your views here.
def home(request):
    return render(request, "home.html")

def todos(request):
    items = TodoItem.objects.all()
    return render(request, "todos.html", {"todos": items})

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            # simpan ke database / kirim email di sini
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            # contoh: Contact.objects.create(name=name, email=email, message=message)

            # kalau request datang dari HTMX, render partial khusus sukses
            if request.headers.get('HX-Request'):
                return render(request, 'partials/contact_success.html')
        else:
            # kalau invalid dan dari HTMX, render ulang form dengan error
            if request.headers.get('HX-Request'):
                return render(request, 'partials/contact_form.html', {'form': form})
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})
