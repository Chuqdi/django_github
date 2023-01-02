from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView
from .models import Book
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect


def index(request):
    return render(request, "index.html")



def register_user(request):
    form = UserCreationForm()
    if request.method =="POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "User Account Created Successfully")
            return redirect("login")
    return render(request, 'auth/register.html', {"form":form})

    



class Dashboard(LoginRequiredMixin, ListView):
    template_name ="auth/dashboard.html"
    model = Book
    context_object_name = "books"


class CreateBook(LoginRequiredMixin, CreateView):
    template_name ="books/create.html"
    model = Book
    fields = ["title", "description","price", "image"]



    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class DetailBook(LoginRequiredMixin, DetailView):
    template_name="books/detail.html"
    model = Book
    



class UpdateBook(LoginRequiredMixin, UpdateView):
    template_name="books/update.html"
    model = Book
    fields = ["title", "description","price", "image"]


    def get_queryset(self):
        if not (self.queryset.id == self.request.id):
            return HttpResponse("YOU ARE NOT AUTHORIZED HERE")



class DeleteBook(LoginRequiredMixin, DeleteView):
    template_name="books/delete.html"
    model = Book
    success_url="dashboard"