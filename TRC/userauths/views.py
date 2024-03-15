from django.shortcuts import render, redirect
from userauths.forms import UserRegisterForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.conf import settings

User = settings.AUTH_USER_MODEL


# Create your views here.
def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save();
            username = form.cleaned_data.get('username')
            messages.success(request, f"Hey {username}, Your account was created successfully.")
            new_user = authenticate(username=form.cleaned_data.get('email'),
                                    password=form.cleaned_data.get('password1')
                                    )
            login(request, new_user)
            return redirect('home')
    else:
        form = UserRegisterForm()

    context = {
        'form': form,
    }

    return render(request, "register.html", context)


def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
        except:
            messages.warning(request, f"User with {email} does not exist")

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Success')
            return redirect('home')
        else:
            messages.warning(request, 'User Dose not Exist')

    context = {}

    return render(request, 'login.html')

def logout_view(request):
    messages.success(request, 'you Signed-Out')
    logout(request)
    return render(request, 'login.html')