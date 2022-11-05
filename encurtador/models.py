from django.db import models
from django.core.validators import URLValidator


class Web_URL(models.Model):
    url = models.TextField(validators=[URLValidator()], null=False)
    count = models.IntegerField(default=0)
    short = models.CharField(max_length=15)

    def __str__(self):
        return self.url