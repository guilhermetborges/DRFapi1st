from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.db.models import Avg



class Base(models.Model):
    criacao = models.DateTimeField(auto_now_add=True)
    atualizacao = models.DateTimeField(auto_now=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Curso(Base):
    titulo = models.CharField(max_length=255)
    url = models.URLField(unique=True)
    media_avaliacoes = models.DecimalField(max_digits=2,decimal_places=1,default=0)
    

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        ordering = ['id']


    def __str__(self):
        return self.titulo
    
class Avaliacao(Base):
    curso = models.ForeignKey(Curso, related_name='avaliacoes', on_delete=models.CASCADE)
    nome = models.CharField(max_length=255)
    email = models.EmailField()
    comentario = models.TextField(blank=True, default='')
    avaliacao = models.DecimalField(max_digits=2, decimal_places=1)

    class Meta:
        verbose_name = 'Avaliação'
        verbose_name_plural = 'Avaliações'
        unique_together = ['email', 'curso']

    
    def __str__(self):
        return f'{self.nome} avaliou o curso {self.curso} com nota {self.avaliacao}'
    

@receiver(post_save, sender=Avaliacao)
@receiver(post_delete, sender=Avaliacao)
def atualizar_media_avaliacoes_curso(sender, instance, **kwargs):
    curso = instance.curso
    media = curso.avaliacoes.all().aggregate(Avg('avaliacao')).get('avaliacao__avg')

    if media is None:
        media = 0

    curso.media_avaliacoes = media
    curso.save()