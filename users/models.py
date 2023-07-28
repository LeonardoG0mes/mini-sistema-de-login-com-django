from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta, timezone

class PerfilUsuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    codigo_autenticacao = models.CharField(max_length=6)
    data_criacao_codigo = models.DateTimeField(auto_now_add=True)
    tempo_expiracao_codigo = models.IntegerField(default=2)  # Tempo em minutos

    def codigo_expirado(self):
        # Obtenha a data e hora atual com fuso horário
        now = datetime.now(timezone.utc)

        # Calcula o momento de expiração do código
        data_expiracao = self.data_criacao_codigo + timedelta(minutes=self.tempo_expiracao_codigo)

        # Verifica se o momento atual é posterior ao momento de expiração
        return now > data_expiracao