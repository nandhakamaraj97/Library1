from django.shortcuts import render, redirect
from .models import Book, Register, Student_Register
from django.contrib import messages


# Create your views here.

def Home(request):
    return render(request, 'index.html')


def Open(request):
    return render(request, 'Home.html')


def Admin_Login(request):
    if 'Admin_Email' not in request.session:
        if request.method == 'POST':
            Email1 = request.POST.get('Email')
            Password1 = request.POST.get('Password')
            try:
                print('aa')
                check = Register.objects.get(Email=Email1, Password=Password1)
                request.session['Admin_Email'] = check.Email
                return render(request, 'Home.html')
            except:
                messages.success(request, 'Not Valid')
                return render(request, 'Login.html')
        return render(request, 'Login.html')
    return redirect('/Open')


def Add_Book(request):
    if request.method == 'POST':
        pro = Book()
        pro.Book_Name = request.POST.get('Book_Name')
        pro.Author_Name = request.POST.get('Author_Name')
        pro.publication = request.POST.get('publication')
        pro.No_of_Pages = request.POST.get('No_of_Pages')
        pro.save()
        return redirect('/Open')
    return render(request, 'Add.html')


def Update_Book(request):
    pro = Book.objects.all()
    context = {'pro': pro}
    return render(request, 'Update.html', context)


def Admin_Logout(request):
    request.session.pop('Admin_Email', None)
    return redirect('/')


def Admin_Register(request):
    try:
        if request.method == 'POST':
            pro = Register()
            pro.Name = request.POST.get('Name')
            pro.Phone = request.POST.get('Phone')
            pro.Email = request.POST.get('Email')
            pro.Password = request.POST.get('Password')
            pro.save()
            return redirect('/Admin_Login')
        return render(request, 'Register.html')
    except:
        messages.success(request, 'Use different Email-ID')
        return render(request, 'Register.html')


def View_Book(request):
    pro = Book.objects.all()
    context = {'pro': pro}
    return render(request, 'View.html', context)


def Delete_Book(request):
    pro = Book.objects.all()
    context = {'pro': pro}
    return render(request, 'Delete.html', context)


def Delete(request, pk):
    pro = Book.objects.get(id=pk)
    pro.delete()
    return redirect('/Delete_Book')


def Update_book(request, pk):
    pro = Book.objects.get(id=pk)
    context = {'p': pro}
    print('asasd')
    if request.method == 'POST':

        if request.POST.get('Book_Name'):
            print('das')
            pro.Book_Name = request.POST.get('Book_Name')
            pro.save()
        elif request.POST.get('Author_Name'):
            pro.Author_Name = request.POST.get('Author_Name')
            pro.save()
        elif request.POST.get('publication'):
            pro.publication = request.POST.get('publication')
            pro.save()
        elif request.POST.get('No_of_Pages'):
            pro.No_of_Pages = request.POST.get('No_of_Pages')
            pro.save()

        return redirect('/Update_Book')
    return render(request, 'Update_Things.html', context)


def Student_Login(request):
    if 'Student_Email' not in request.session:
        if request.method == 'POST':
            Email1 = request.POST.get('Email')
            Password1 = request.POST.get('Password')
            try:
                check = Student_Register.objects.get(Email=Email1, Password=Password1)
                request.session['Student_Email'] = check.Email
                return render(request, 'Student_Home.html')
            except:
                messages.success(request, 'Not Valid')
                return render(request, 'Student_Login.html')
        return render(request, 'Student_Login.html')
    return redirect('/Student_Home')


def Student_Registers(request):
    try:
        if request.method == 'POST':
            pro = Student_Register()
            pro.Name = request.POST.get('Name')
            pro.Phone = request.POST.get('Phone')
            pro.Email = request.POST.get('Email')
            pro.Password = request.POST.get('Password')
            pro.save()
            return redirect('/Student_Login')
        return render(request, 'Student_Register.html')
    except:
        messages.success(request, 'Use different Email-ID')
        return render(request, 'Student_Register.html')


def Student_Home(request):
    return render(request, 'Student_Home.html')


def Student_Logout(request):
    request.session.pop('Student_Email', None)
    return redirect('/')


def Student_Book(request):
    pro = Book.objects.all()
    context = {'pro': pro}
    return render(request, 'View_Boo.html', context)
