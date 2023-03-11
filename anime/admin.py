from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from .models import Anime, Series, Genre


class AnimeAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'image',
        'number_of_series',
    )

    search_fields = ('title', )
    @staticmethod
    def number_of_series(instance):
        return instance.series_set.count()

    def image(self, obj):
        if not obj.img_url:
            return '-'
        return format_html(
            f"<img style='width: 60px; height: 60px'  loading='lazy'"
            f"src='{obj.img_url}'>"
        )


class SeriesAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'preview_',
        'season',
        'series_number',
        'has_video_360',
        'has_video_480',
        'has_video_720',
        'has_video_1080',
        'anime_link',
    )

    search_fields = ('name',)

    def preview_(self, obj):
        if not obj.preview:
            return '-'
        return format_html(
            f"<img style='width: 60px; height: 60px'  loading='lazy'"
            f"src='{obj.preview}'>"
        )

    def has_video_360(self, obj):
        return bool(obj.video_360)

    def has_video_480(self, obj):
        return bool(obj.video_480)

    def has_video_720(self, obj):
        return bool(obj.video_720)

    def has_video_1080(self, obj):
        return bool(obj.video_1080)

    def anime_link(self, obj):
        return format_html('<a href="{}">{}</a>'.format(
            reverse("admin:anime_anime_change", args=(obj.anime.pk,)),
            obj.anime.title
        ))

    has_video_360.boolean = True
    has_video_480.boolean = True
    has_video_720.boolean = True
    has_video_1080.boolean = True


admin.site.register(Anime, AnimeAdmin)
admin.site.register(Series, SeriesAdmin)
admin.site.register(Genre)
