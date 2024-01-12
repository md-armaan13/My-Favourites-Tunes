from django.db import models
from django.core.validators import MinValueValidator
from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError


def validate_file_size(file) :
    max_size_mb = 10

    if file.size > max_size_mb * 1024 * 1024:
        raise ValidationError(f'File size should not exceed {max_size_mb} MB.')


class Artist (models.Model) :
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='artists-images', blank=True, null=True ,validators=[validate_file_size])
    age = models.IntegerField(validators=[MinValueValidator(0,message='Age should be positive')])
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    listners = models.IntegerField(validators=[MinValueValidator(0,message='Listners should be positive')])

    def __str__(self) -> str:
        return self.name
    

class Song (models.Model) :
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='songs-images/',null=True, blank=True,validators=[validate_file_size])
    streams = models.IntegerField(validators=[MinValueValidator(0,message='streams should be positive')])
    likes = models.IntegerField(validators=[MinValueValidator(0,message='streams should be positive')])
    release_date = models.DateField()
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)   
   
    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ["release_date"]

    