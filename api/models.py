from django.db import models

# Create your models here.

class Property(models.Model):

    location=models.CharField(max_length=200)

    price=models.PositiveIntegerField()

    image=models.ImageField(upload_to="propertyimages",null=True)

    PROPERTY_CHOICES=(
    ("house","house"),
    ("land","land"),
    ("appartment","appartment"),
    )

    property_type=models.CharField(max_length=200,choices=PROPERTY_CHOICES,default="house")

    bedroom_count=models.PositiveIntegerField()

    square_footage=models.PositiveIntegerField()

    contact=models.CharField(max_length=200)

    created_date=models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:

        return  self.location


