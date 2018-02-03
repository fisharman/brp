# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Annotations(models.Model):
    id = models.IntegerField(primary_key=True)
    osis = models.TextField(unique=True)
    link = models.TextField(unique=True)
    content = models.TextField()

    class Meta:
        managed = False
        db_table = 'annotations'
        unique_together = (('osis', 'link'),)


class Books(models.Model):
    number = models.IntegerField(primary_key=True)
    osis = models.TextField()
    human = models.TextField()
    chapters = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'books'

    def __str__(self):
        return self.human


class Chapters(models.Model):
    id = models.IntegerField(primary_key=True)
    reference_osis = models.TextField(unique=True)
    reference_human = models.TextField()
    content = models.TextField()
    previous_reference_osis = models.TextField(blank=True, null=True)
    previous_reference_human = models.TextField(blank=True, null=True)
    next_reference_osis = models.TextField(blank=True, null=True)
    next_reference_human = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chapters'


class Metadata(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField(unique=True)
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'metadata'


class Verses(models.Model):
    id = models.IntegerField(primary_key=True)
    book = models.CharField(max_length=7, blank=True, null=True)
    verse = models.FloatField(blank=True, null=True)
    unformatted = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'verses'
