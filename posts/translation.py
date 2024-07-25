from modeltranslation.translator import register, TranslationOptions, translator
from .models import Project, ProjectImage, Comment, Tariff, Project_Type, Order


class ProjectTranslationOptions(TranslationOptions):
    fields = ['title', 'description']


translator.register(Project, ProjectTranslationOptions)


@register(Comment)
class CommentTranslationOptions(TranslationOptions):
    fields = ['comment']


@register(Tariff)
class TariffTranslationOptions(TranslationOptions):
    fields = ['title', 'description']


@register(Project_Type)
class ProjectTypeTranslationOptions(TranslationOptions):
    fields = ['title', 'description']
