from django.contrib.auth.models import User
from django.db import models

POSTO_GRADUACAO_CHOICES = [
    ("SD", "Soldado"),
    ("CB", "Cabo"),
    ("SGT", "Sargento"),
    ("ST", "Subtenente"),
    ("ASP", "Aspirante"),
    ("TEN", "Tenente"),
    ("CAP", "Capitão"),
    ("MAJ", "Major"),
    ("TC", "Tenente-Coronel"),
    ("CEL", "Coronel"),
]

FUNCAO_CHOICES = [
    ("PATRULHEIRO", "Patrulheiro"),
    ("MOTORISTA", "Motorista"),
    ("ENCARREGADO", "Encarregado"),
    ("CHEFE", "Chefe"),
    ("ADMINISTRATIVO", "Administrativo"),
    ("COORDENADOR", "Coordenador"),
]

TIPO_SANGUINEO_CHOICES = [
    ("A", "A"),
    ("B", "B"),
    ("AB", "AB"),
    ("O", "O"),
]

FATOR_RH_CHOICES = [
    ("+", "Positivo"),
    ("-", "Negativo"),
]

SEXO_CHOICES = [
    ("M", "Masculino"),
    ("F", "Feminino"),
]


class Policial(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nome_completo = models.CharField(max_length=150)
    nome_guerra = models.CharField(max_length=150)
    nome_mae = models.CharField(max_length=150)
    nome_pai = models.CharField(max_length=150, blank=True, null=True)
    data_nascimento = models.DateField()
    matricula = models.CharField(max_length=20, unique=True)
    identidade_militar = models.CharField(max_length=20, unique=True)
    cpf = models.CharField(max_length=14, unique=True)
    posto_graduacao = models.CharField(max_length=4, choices=POSTO_GRADUACAO_CHOICES)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    tipagem_sanguinea = models.CharField(max_length=3, choices=TIPO_SANGUINEO_CHOICES)
    fator_rh = models.CharField(max_length=1, choices=FATOR_RH_CHOICES)
    data_ingresso = models.DateField()
    foto = models.ImageField(upload_to="fotos_policiais/", blank=True, null=True)
    funcao = models.CharField(max_length=20, choices=FUNCAO_CHOICES)
    endereco = models.TextField()
    telefone = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.nome_completo} - {self.posto_graduacao}"
