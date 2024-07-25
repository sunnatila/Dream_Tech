from django.contrib import admin
from .models import Project, Project_Type, Order, Comment, Tariff, ProjectImage
from modeltranslation.admin import TabbedTranslationAdmin

from . import translation


@admin.register(Project)
class ProjectAdmin(TabbedTranslationAdmin):
    list_display = ('title',)
    list_filter = ('created_at',)


@admin.register(Project_Type)
class ProjectTypeAdmin(TabbedTranslationAdmin):
    list_display = ('value', 'title', 'description')


@admin.register(ProjectImage)
class ProjectImageAdmin(admin.ModelAdmin):
    list_display = ('project', 'created_at')


@admin.register(Tariff)
class TariffAdmin(TabbedTranslationAdmin):
    list_display = ('title', 'start_amount')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'phone', 'project_type', 'tariff', 'status', 'create_time')
    list_filter = ('status', 'create_time')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'project', 'date', 'rank')
    list_filter = ('rank', 'date')
