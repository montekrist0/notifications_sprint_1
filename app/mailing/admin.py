from django.contrib import admin
from django.utils.safestring import mark_safe
from sorl.thumbnail import get_thumbnail

from .models import EmailTemplateContent, EmailTemplateImage, EmailTemplateContext, EmailAssembled


class TemplateImageInline(admin.TabularInline):
    model = EmailTemplateImage
    extra = 0
    readonly_fields = ("get_thumb",)

    def get_thumb(self, obj):
        url = get_thumbnail(obj.image, "100x100", crop="center", quality=99)
        return mark_safe(f"""<img src={url.url} />""")

    get_thumb.short_description = "image"


@admin.register(EmailTemplateContent)
class TemplateAdmin(admin.ModelAdmin):
    inlines = (TemplateImageInline,)

    list_display = (
        "admin_title",
        "title",
    )


@admin.register(EmailTemplateImage)
class TemplateImageAdmin(admin.ModelAdmin):
    list_display = (
        "admin_title",
        "image",
        "template",
        "get_thumb",
    )

    def get_thumb(self, obj):
        url = get_thumbnail(obj.image, "100x100", crop="center", quality=99)
        return mark_safe(f"""<img src={url.url} />""")

    get_thumb.short_description = "image"


@admin.register(EmailTemplateContext)
class TemplateContext(admin.ModelAdmin):
    list_display = ("admin_title",)


@admin.register(EmailAssembled)
class AssembledEmail(admin.ModelAdmin):
    list_display = ("template", "context",)
    readonly_fields = ("text",)
