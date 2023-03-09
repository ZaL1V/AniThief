from django.db import models



class Anime(models.Model):
    title = models.CharField(max_length=512)
    description = models.TextField()
    img_url = models.URLField()
    genre = models.ManyToManyField('anime.Genre', blank= True, null= True)

    def __str__(self):
        return self.title


class Series(models.Model):
    name = models.CharField(max_length=512, null=True, blank=True)
    preview = models.URLField(blank=True, null=True)
    season = models.PositiveIntegerField()
    series_number = models.PositiveIntegerField()
    video_360 = models.URLField(blank=True, null=True)
    video_480 = models.URLField(blank=True, null=True)
    video_720 = models.URLField(blank=True, null=True)
    video_1080 = models.URLField(blank=True, null=True)
    anime = models.ForeignKey('anime.Anime', on_delete=models.CASCADE)

    def __str__(self):
        return self.name




class Genre(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name
