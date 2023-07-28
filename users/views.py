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
from django.contrib.auth.forms import PasswordChangeForm
from django.core.mail import send_mail
from django.utils import timezone 
from .models import PerfilUsuario
import random
import string

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

        # Gerar o código de autenticação
        code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

        # Envie o código de autenticação por email
        subject = 'Código de Autenticação'
        from_email = 'seu_email@gmail.com'  # Substitua pelo seu email
        message = f'Olá,\n\nSeu código de autenticação é: {code}\n\n' \
          f'Utilize este código para completar o processo de cadastro.\n\n' \
          f'Este código é válido por 2 minutos. Caso tenha expirado, solicite um novo código ' \
          f'no link de reenvio.\n\n' \
          f'Obrigado!\n\nEquipe do Seu Aplicativo'
        to_email = email
        send_mail(subject, message, from_email, [to_email])

        # Crie o novo usuário usando User.objects.create_user
        user = User.objects.create_user(username=username, email=email, password=password)

        # Crie o perfil de usuário associado ao usuário criado
        perfil_usuario = PerfilUsuario.objects.create(user=user, codigo_autenticacao=code)

        # Redirecione para a página onde o usuário digitará o código de autenticação
        return redirect('verificar_codigo', email=email)


def verificar_codigo(request, email):
    if request.method == "POST":
        codigo_digitado = request.POST.get('codigo')

        # Verifique se o código digitado pelo usuário corresponde ao código salvo no perfil do usuário
        perfil_usuario = PerfilUsuario.objects.filter(user__email=email, codigo_autenticacao=codigo_digitado).first()

        if perfil_usuario and not perfil_usuario.codigo_expirado():
            # Autenticação bem-sucedida, faça o login do usuário e redirecione para a página inicial
            login_django(request, perfil_usuario.user)

            # Exclua o perfil do usuário após a autenticação bem-sucedida
            perfil_usuario.delete()

            return redirect('home')
        else:
            if perfil_usuario:
                # Caso o código tenha expirado, exclua o perfil do usuário
                perfil_usuario.delete()

            messages.error(request, 'Código de autenticação inválido ou expirado. Peça para reenviar o código.')
            return render(request, 'verificar_codigo.html', {'email': email})

    return render(request, 'verificar_codigo.html', {'email': email})

@login_required(login_url='/auth/login/')
def reenviar_codigo(request, email):
    # Verifique se o usuário tem um perfil de usuário associado ao email fornecido
    perfil_usuario = PerfilUsuario.objects.filter(user__email=email).first()

    if perfil_usuario:
        # Gerar um novo código de autenticação
        novo_codigo = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

        # Atualizar o código existente no banco de dados com o novo código
        perfil_usuario.codigo_autenticacao = novo_codigo
        perfil_usuario.data_criacao_codigo = timezone.now()  # Atualizar a data de criação do código
        perfil_usuario.save()

        # Envie o novo código de autenticação por email
        subject = 'Novo Código de Autenticação'
        from_email = 'seu_email@gmail.com'  # Substitua pelo seu email
        message = f'Seu novo código de autenticação é: {novo_codigo}'
        to_email = email
        send_mail(subject, message, from_email, [to_email])

        messages.success(request, 'Novo código de autenticação enviado. Verifique seu email.')
    else:
        # Se o perfil de usuário não existir, crie um novo perfil de usuário associado ao email fornecido
        user = User.objects.filter(email=email).first()

        if user:
            novo_codigo = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
            perfil_usuario = PerfilUsuario.objects.create(user=user, codigo_autenticacao=novo_codigo)
            
            # Envie o novo código de autenticação por email
            subject = 'Novo Código de Autenticação'
            from_email = 'seu_email@gmail.com'  # Substitua pelo seu email
            message = f'Seu novo código de autenticação é: {novo_codigo}'
            to_email = email
            send_mail(subject, message, from_email, [to_email])

            messages.success(request, 'Novo código de autenticação enviado. Verifique seu email.')
        else:
            messages.error(request, 'Não foi possível encontrar um perfil de usuário associado a este email.')

    # Verifique se o usuário está autenticado antes de redirecionar
    if request.user.is_authenticated:
        return redirect('verificar_codigo', email=email)
    else:
        return redirect('home')
    
def excluir_perfil_usuario(email):
    try:
        perfil_usuario = PerfilUsuario.objects.get(user__email=email)
        perfil_usuario.delete()
    except PerfilUsuario.DoesNotExist:
        pass

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

@login_required(login_url='/auth/login/')
def trocar_senha(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Sua senha foi alterada com sucesso!')
            return redirect('home')
        else:
            errors = form.errors
            for field, field_errors in errors.items():
                for error in field_errors:
                    messages.error(request, error)

    else:
        form = PasswordChangeForm(request.user)
    
    return render(request, 'trocar_senha.html', {'form': form})