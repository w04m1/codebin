from django.db import models

from users.models import User


class Snippet(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    language = models.CharField(max_length=50)
    code = models.TextField()
    published = models.DateTimeField(auto_now_add=True)
    public = models.BooleanField(default=False)

    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} ({self.language})"

    class Meta:
        ordering = ("-published",)


class Comment(models.Model):
    text = models.TextField()
    published = models.DateTimeField(auto_now_add=True)

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    snippet = models.ForeignKey(Snippet, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.owner}: {self.text[:20]}"

    class Meta:
        ordering = ("-published",)


class Reaction(models.Model):
    LIKE = True
    DISLIKE = False

    REACTION_CHOICES = (
        (LIKE, "Like"),
        (DISLIKE, "Dislike"),
    )

    reaction = models.BooleanField(choices=REACTION_CHOICES)

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    snippet = models.ForeignKey(Snippet, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.owner}: {self.reaction}"

    class Meta:
        unique_together = ("owner", "snippet")
