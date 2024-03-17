from django.db import models

CHOICES = [
    ("content", "Content"),
    ("video", "Video"),
]


class Page(models.Model):
    type = models.CharField(max_length=15, choices=CHOICES)


class Tutorial(models.Model):
    page = models.ForeignKey(Page, on_delete=models.CASCADE, related_name='tutorials')
    content = models.TextField()

    def __str__(self):
        return self.content


class Video(models.Model):
    page = models.ForeignKey(Page, on_delete=models.CASCADE, related_name='videos')
    video_url = models.URLField()

    def __str__(self):
        return self.video_url
