from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth.password_validation import validate_password, CommonPasswordValidator, MinimumLengthValidator
from django.core.exceptions import ValidationError


def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_username = User.objects.filter(username=username).first()
        user_email = User.objects.filter(email=email).first()

        if user_username:
            messages.error(request, 'Usuário já existe')
            return redirect('cadastro')

        elif user_email:
            messages.error(request, 'Endereço de e-mail já está sendo usado')
            return redirect('cadastro')

        # Verificar se todos os campos foram preenchidos
        if not username or not email or not password:
            messages.error(request, 'Todos os campos devem ser preenchidos')
            return redirect('cadastro')

        try:
            # Adicione os validadores personalizados na lista de validadores
            validate_password(password, user=User(username=username), password_validators=[
                MinimumLengthValidator(),
                CommonPasswordValidator(),
                # Outros validadores personalizados podem ser adicionados aqui
            ])
        except ValidationError as e:
            error_messages = [str(error) for error in e]
            messages.error(request, ', '.join(error_messages))
            return redirect('cadastro')

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        messages.success(request, 'Usuário cadastrado com sucesso!')
        return redirect('login')




def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')

    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:
            login_django(request, user)
            return redirect('/auth/home')

        else:
            messages.error(request, 'Usuário ou senha incorretos')
            return redirect('login')

@login_required(login_url='/auth/login/')
def home(request):
    if request.method == 'POST':
        logout(request)
        return redirect('/auth/login')

    return render(request, 'home.html')



