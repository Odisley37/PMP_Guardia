from django.conf import settings
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


class Agressor(models.Model):
    nome_completo = models.CharField(max_length=150)
    identidade = models.CharField(max_length=20)
    cpf = models.CharField(max_length=14, unique=True)
    data_nascimento = models.DateField()
    endereco = models.TextField()
    latitude = models.DecimalField(
        max_digits=9, decimal_places=6, null=True, blank=True
    )
    longitude = models.DecimalField(
        max_digits=9, decimal_places=6, null=True, blank=True
    )
    foto = models.ImageField(upload_to="fotos_agressores/", blank=True, null=True)

    def __str__(self):
        return self.nome_completo


from django.db import models

VTR_CHOICES = [
    ("VTR-01", "Viatura 01"),
    ("VTR-02", "Viatura 02"),
    ("VTR-03", "Viatura 03"),
]

FUNCAO_CHOICES = [
    ("COMANDANTE", "Comandante"),
    ("MOTORISTA", "Motorista"),
    ("PATRULHEIRO", "Patrulheiro"),
]


class Guarnicao(models.Model):
    viatura = models.CharField(max_length=10, choices=VTR_CHOICES)
    inicio_servico = models.DateTimeField()
    fim_servico = models.DateTimeField(null=True, blank=True)
    km_inicial = models.PositiveIntegerField()
    km_final = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.viatura} - {self.inicio_servico.date()}"


class GuarnicaoIntegrante(models.Model):
    guarnicao = models.ForeignKey(
        Guarnicao, on_delete=models.CASCADE, related_name="integrantes"
    )
    policial = models.ForeignKey(Policial, on_delete=models.CASCADE)
    funcao = models.CharField(max_length=20, choices=FUNCAO_CHOICES)

    def __str__(self):
        return f"{self.policial.nome_guerra} - {self.funcao}"


SIM_NAO_CHOICES = [
    ("SIM", "Sim"),
    ("NAO", "Não"),
]


class Assistida(models.Model):
    numero_processo = models.CharField(primary_key=True, max_length=30)
    foto = models.ImageField(upload_to="fotos_assistidas/", blank=True, null=True)
    nome_completo = models.CharField(max_length=150)
    nome_mae = models.CharField(max_length=150)
    nome_pai = models.CharField(max_length=150, blank=True, null=True)
    cpf = models.CharField(max_length=14, unique=True)
    data_nascimento = models.DateField()
    identidade = models.CharField(max_length=20)
    endereco = models.TextField()
    latitude = models.DecimalField(
        max_digits=9, decimal_places=6, null=True, blank=True
    )
    longitude = models.DecimalField(
        max_digits=9, decimal_places=6, null=True, blank=True
    )
    agressor = models.ForeignKey(Agressor, on_delete=models.CASCADE)
    guarnicao = models.ForeignKey(
        Guarnicao, on_delete=models.SET_NULL, null=True, blank=True
    )
    data_visita = models.DateField()
    validade_processo = models.DateField()
    agressor_citado = models.CharField(max_length=3, choices=SIM_NAO_CHOICES)
    ultima_visita = models.DateField()
    ocorrencia = models.TextField(blank=True, null=True)
    cancelar_atendimento = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.numero_processo} - {self.nome_completo}"
