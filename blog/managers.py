from django.db import models


# change behavior and attribute model manager
class ArticleManger(models.Manager):
    def counter(self):
        return len(self.all())

    def published(self):
        return self.filter(is_published=True)

# customize queryset


class CustomArticleManger(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published=True)
