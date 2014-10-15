# encoding: utf-8
# Author: Juliano Fischer Naves
# julianofischer at gmail dot com
# April, 2014

from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class StudentClass(models.Model):
    name = models.CharField(max_length=30,verbose_name='Turma')
    
    def __unicode__(self):
        return self.name
        
    class Meta:
        #Translators: The student class
        verbose_name = _("Turma")

class Student(models.Model):
    cpf = models.CharField(max_length=11,verbose_name="CPF")
    name = models.CharField(max_length=60,verbose_name="Nome")
    mother_name = models.CharField(max_length=60,verbose_name="Nome da mãe")
    father_name = models.CharField(max_length=60,verbose_name="Nome do pai")
    father_phone = models.CharField(max_length=60,verbose_name="Telefone do pai")
    mother_phone = models.CharField(max_length=11,verbose_name="Telefone da mãe")
    home_phone = models.CharField(max_length=11,verbose_name="Telefone de casa")
    student_class = models.ForeignKey('StudentClass',verbose_name="Turma")
    
    def __unicode__(self):
        return self.name
        
    class Meta:
        verbose_name = _("Estudante")
        verbose_name_plural = _("Estudantes")

#Ocorrência    
class Incident(models.Model):
    title = models.CharField(max_length=50,verbose_name=u"Título")
    type = models.ForeignKey('IncidentType',verbose_name="Tipo")
    description = models.TextField(verbose_name=u"Descrição")
    measure_taken = models.TextField(verbose_name="Medida tomada")
    student = models.ForeignKey('Student',verbose_name="Estudante")
    student_class = models.ForeignKey('StudentClass',verbose_name='Turma')
    date_time = models.DateTimeField(verbose_name='Data e hora')
    archived = models.BooleanField(default=False,verbose_name='Arquivado')
    
    def __unicode__(self):
        return self.title
        
    def save(self, *args, **kwargs):
        if self.pk is None:
            self.student_class = self.student.student_class
            super(Incident, self).save(*args,**kwargs)
        
        
    class Meta:
        verbose_name = _(u"Ocorrência")
        verbose_name_plural = _(u"Ocorrências")

class IncidentType(models.Model):
    title = models.CharField(max_length=30,verbose_name=u"Tipo de Ocorrência")
    
    def __unicode__(self):
        return self.title
        
    class Meta:
        verbose_name=("Tipo")
